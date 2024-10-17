# FastAPI

```sh
pip install fastapi
```
## 🚀 Project Structure

```text
/
├── config/
│   ├── __init__.py
│   └── database.py
├── middlewares/
│   ├── __init__.py
│   ├── error_handler.py
│   └── jwt_bearer.py   
├── models/
│   ├── __init__.py
│   └── movie.py
├── routers/
│   ├── __init__.py
│   ├── movie.py
│   └── user.py
├── schemas/
│   ├── __init__.py
│   ├── movie.py
│   └── user.py
├── services/
│   ├── __init__.py
│   └── movie.py
├── utils/
│   ├── __init__.py
│   └── jwt_manager.py
├── .editorconfig
├── .gitignore
├── database.sqlite
├── LICENCE.md
├── main.py
├── READMEmd
└── requirements.txt
```

## Instalar `uvicorn`:

```sh
pip install uvicorn
```

## Ejecutar el comando para correr el servidor

```sh
uvicorn main:app --reload --port 5000 --host 0.0.0.0
```

## Documentación interactiva de APIS

Ahora ve a http://127.0.0.1:8000/docs

Verás la documentación automática e interactiva de la API (proveída por [Swagger UI]('https://github.com/swagger-api/swagger-ui'))

## Función para generar tokens

_Instalar libraria PyJWT_

```sh
pip install pyjwt

```

## ¿Qué es un ORM?

_Es un librería que nos permite la manipulación de tablas de una base de datos como si fueran ojetos de nuestra aplicaión._

Ejemplo:

| Movie        |              |
| :-----------:| :-----------:|
| id           | int          |
| title        | varchar      |
| overview     | varchar      |
| year         | int          |
| rating       | float        |
| category     | varchar      |

```py

class Movie(Base):
    __tablename__='movies'

    id=column(Integer,primary_key=True)
    title=column(String)
    overview=column(String)
    year=column(Integer)
    rating=column(Float)
    category=column(String)

```

## ¿Qué es SQLAlchemy?

_Es una librería para Python que facilita el acceso a una base de datos relacional mapeando tablas SQL  a clases._

## Instalación y configuración de SQLAlchemy

```sh
pip install sqlalchemy
```

## Craer el archivo requirements.txt para guardar la lista de modulos que utiliza la app

```sh
pip freeze > requirements.txt

```
