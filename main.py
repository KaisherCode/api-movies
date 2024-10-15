from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My FastAPI"
app.version = "0.0.1"

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview":"En un exuberante planeta llamado pandora viven lso Navi",
        "year":"2009",
        "rating":"7.8",
        "category":"Acción",
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
  }
]

@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>Hola Mundo!<h1/>')

@app.get('/movies',tags=['movies'])
def get_movies():
    return movies