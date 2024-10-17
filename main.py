from fastapi import FastAPI
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler
from jwt_manager import create_token
from routers.movie import movie_router

app = FastAPI()
app.title = "My FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    email: str
    password: str


@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>Hola Mundo!<h1/>')

# Login

@app.post('/login',tags=['auth'])
def login(user:User):
    if user.email=="admin@gmail.com" and user.password=="admin":
        token:str=create_token(user.dict())
        return JSONResponse(status_code=200,content=token)  



