from fastapi import APIRouter
from modelss.movie import Movie
from fastapi import  Path, Query, HTTPException, Depends
from fastapi.responses import  JSONResponse
from pydantic import BaseModel, Field
from typing import  List
from config.database import session
from modelss.movie import Movie as MovieModelss
from fastapi.encoders import jsonable_encoder
from fastapi.logger import logger
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie
movie_router= APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies():
    db = session()
    result = db.query(MovieModelss).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], status_code=404)
def get_movies_id(id: int = Path(ge=1, le=2000)):
    db = session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(min_length=5, max_length=10)):
    db = session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def include_movie(movie: Movie):
    db = session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha agregado la película correctamente"})

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_by_id(id: int, movie: Movie):
    db = session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    
    try:
       MovieService(db).update_movie(id, movie)
       db.commit()
       return JSONResponse(status_code=200, content={"message": "Se ha modificado la pelicula"})
    except Exception as e:
       logger.error(f"Error updating movie: {e}")
       db.rollback()
       raise HTTPException(status_code=500, detail="Error actualizando la película")
  
@movie_router.delete('/movies/{id}', tags=['movies'], status_code=200)
def del_by_id(id: int):
    db = session()
    result: MovieModelss= db.query(MovieModelss).filter(MovieModelss.id==id).first()
    if not result:
        return JSONResponse(status_code=404, content='No se ha encontrado la pelicula')
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})