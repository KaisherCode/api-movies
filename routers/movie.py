from fastapi import APIRouter
from fastapi import Path,Query,Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()




@movie_router.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200,dependencies=[Depends(JWTBearer())])
def get_movies()->List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.get('/movies/{id}',tags=['movies'],response_model=Movie)
def get_movie_by_id(id:int=Path(ge=1,le=2000))->Movie:
    db = Session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"Movie no encontrado"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.get('/movies/',tags=['movies'],response_model=List[Movie])
def filter_movies_by_category(category:str=Query(min_length=5,max_length=25))->List[Movie]:
    db = Session()
    result = MovieService(db).filter_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=404,content={"message":"Categoria no encontrado"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.post('/movies',tags=['movies'],response_model=dict,status_code=201)
def create_movies(movie:Movie)->dict:
    db=Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201,content={'message':'Se ha registrado la película.'})

@movie_router.put('/movies/{id}',tags=['movies'],response_model=dict,status_code=200)
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
        
@movie_router.delete('/movies/{id}',tags=['movies'],response_model=dict,status_code=200)
def delete_movie(id:int)->dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404,content={"message":"Id no encontrado, ingrese id válido"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200,content={'message':'Se ha eliminado la película.'})