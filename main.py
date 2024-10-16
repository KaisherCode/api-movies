from fastapi import FastAPI,Body
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
        "category":"Action",
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
    return movies

@app.get('/movies/{id}',tags=['movies'])
def get_movie_by_id(id:int):
    for item in movies:
        if item['id']==id:
            return item
    return []

@app.get('/movies/',tags=['movies'])
def filter_movies_by_category(category:str,year:int):
    return [item for item in movies if item['category']==category]

@app.post('/movies',tags=['movies'])
def create_movies(id:int=Body(),title:str=Body(),overview:str=Body(),year:int=Body(),rating:float=Body(),category:str=Body()):
    movies.append({
        "id":id,
        "title":title,
        "overview": overview,
        "year": year,
        "category":category,
    })
    return movies

@app.put('/movies/{id}',tags=['movies'])
def update_movie(id: int,title: str=Body(),overview:str=Body(),year:int=Body(),category:str=Body()):
    for item in movies:
        if item['id']==id:
            item['title']=title,
            item['overview']=overview,
            item['year']=year,
            item['category']=category,
            return movies