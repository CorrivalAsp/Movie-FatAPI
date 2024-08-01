
from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(ge=1900, le=2100)
    rating: float = Field(ge=1, le=10.0)
    category: str = Field(min_length=5, max_length=10)

    class Config:
        schema_extra = {
            "example": {
                "title": "La pelicula",
                "overview": "Descripción de la película",
                "year": 2024,
                "rating": 9.8,
                "category": "Acción"
            }
        }

