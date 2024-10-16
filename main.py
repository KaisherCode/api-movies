from fastapi import FastAPI,Body,Path,Query
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel,Field,ConfigDict
from typing import Optional

app = FastAPI()
app.title = "My FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int]=None
    title: str = Field(min_length=5,max_length=15)
    overview: str = Field(min_length=15,max_length=50)
    year: int = Field(le=2024)
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
        "year":"2009",
        "rating":"7.8",
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

@app.get('/movies',tags=['movies'])
def get_movies():
    return JSONResponse(content=movies)

@app.get('/movies/{id}',tags=['movies'])
def get_movie_by_id(id:int=Path(ge=1,le=2000)):
    for item in movies:
        if item['id']==id:
            return JSONResponse(content=item)
    return JSONResponse(content=[])

@app.get('/movies/',tags=['movies'])
def filter_movies_by_category(category:str=Query(min_length=5,max_length=50)):
    data=[item for item in movies if item['category']==category]
    return JSONResponse(content=data)

@app.post('/movies',tags=['movies'])
def create_movies(movie:Movie):
    movies.append(movie)
    return JSONResponse(content={'message':'Se ha registrado la película.'})

@app.put('/movies/{id}',tags=['movies'])
def update_movie(id:int,movie:Movie):
    for item in movies:
        if item["id"]==id:
            item['title']=movie.title
            item['overview']=movie.overview
            item['year']=movie.year
            item['rating']=movie.rating
            item['category']=movie.category
            return JSONResponse(content={"message":"Se ha actualizado la película."})
        
@app.delete('/movies/{id}',tags=['movies'])
def delete_movie(id:int):
    for item in movies:
        if item['id']==id:
            movies.remove(item)
            return JSONResponse(content={'message':'Se ha eliminado la película.'})
        
        
