from fastapi import FastAPI
import uvicorn
from os import getenv
from fastapi.responses import HTMLResponse
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "My FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>Hola Mundo!<h1/>')

if __name__=="__main__":
    port = int(getenv("PORT",8000))
    uvicorn.run("main:app",host="0.0.0.0",port=port,reload=True)



