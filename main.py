from fastapi import FastAPI,Path,Query,Depends
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel,Field,ConfigDict
from typing import Optional,List
from config.database import Session,engine,Base
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
from jwt_manager import create_token

app = FastAPI()
app.title = "My FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    email: str
    password: str

class Movie(BaseModel):
    id: Optional[int]=None
    title: str = Field(min_length=5,max_length=15)
    overview: str = Field(min_length=15,max_length=200)
    year: int = Field()
    rating: float = Field(ge=1,le=10)
    category: str = Field(min_length=5,max_length=25)
    
    model_config = ConfigDict(
        json_schema_extra = {
        'examples': [
                {
                    "id": 1,
                    "title": "Mi pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year":2022,
                    "rating": 9.8,
                    "category": "Acción"
                }
            ]
    })

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview":"En un exuberante planeta llamado pandora viven lso Navi",
        "year":2009,
        "rating":7.8,
        "category":"Action"
    },
    {
    "id": 2,
    "title": "Inception",
    "overview": "A thief who steals information by infiltrating the subconscious is offered a chance to have his criminal history erased as payment for the implantation of an idea into the mind of a CEO.",
    "year": 2010,
    "rating": 8.8,
    "category": "Sci-Fi, Action, Adventure"
  },
  {
    "id": 3,
    "title": "The Dark Knight",
    "overview": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
    "year": 2008,
    "rating": 9.0,
    "category": "Action, Crime, Drama"
  },
  {
    "id": 4,
    "title": "The Godfather",
    "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    "year": 1972,
    "rating": 9.2,
    "category": "Crime, Drama"
  },
  {
    "id": 5,
    "title": "El secreto de sus ojos",
    "overview": "No se llevó, de manera incomprensible e injustísima, el máximo galardón del reciente Festival de San Sebastián, pero da lo mismo.",
    "year": 2009,
    "rating": 8.9,
    "category": "Action"
  }
]

@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>Hola Mundo!<h1/>')

# Login

@app.post('/login',tags=['auth'])
def login(user:User):
    if user.email=="admin@gmail.com" and user.password=="admin":
        token:str=create_token(user.dict())
        return JSONResponse(status_code=200,content=token)  

@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200,dependencies=[Depends(JWTBearer())])
def get_movies()->List[Movie]:
    db = Session()
    result = db.query(MovieModel).all()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@app.get('/movies/{id}',tags=['movies'],response_model=Movie)
def get_movie_by_id(id:int=Path(ge=1,le=2000))->Movie:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id==id).first()
    if not result:
        return JSONResponse(status_code=404,content={"message":"Movie no encontrado"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@app.get('/movies/',tags=['movies'],response_model=List[Movie])
def filter_movies_by_category(category:str=Query(min_length=5,max_length=25))->List[Movie]:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category==category).all()
    if not result:
        return JSONResponse(status_code=404,content={"message":"Categoria no encontrado"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@app.post('/movies',tags=['movies'],response_model=dict,status_code=201)
def create_movies(movie:Movie)->dict:
    db=Session()
    new_movie=MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201,content={'message':'Se ha registrado la película.'})

@app.put('/movies/{id}',tags=['movies'],response_model=dict,status_code=200)
def update_movie(id:int,movie:Movie)->dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id==id).first()
    if not result:
        return JSONResponse(status_code=404,content={"message":"Id no encontrado, ingrese un id válido"})
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(status_code=200,content={"message":"Se ha actualizado la película."})
        
@app.delete('/movies/{id}',tags=['movies'],response_model=dict,status_code=200)
def delete_movie(id:int)->dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404,content={"message":"Id no encontrado, ingrese id válido"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200,content={'message':'Se ha eliminado la película.'})


