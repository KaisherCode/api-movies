from pydantic import BaseModel,Field,ConfigDict
from typing import Optional

class Movie(BaseModel):
    id: Optional[int]=None
    title: str = Field(min_length=5,max_length=25)
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