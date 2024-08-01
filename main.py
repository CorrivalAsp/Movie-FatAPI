from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router 
from routers.user import user_router as user_login_router
app = FastAPI()
app.title = "Mi primer proyecto con FastAPI"
app.version = "0.0.1"

app.middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_login_router)

Base.metadata.create_all(bind=engine)




movies = [
    {
        'id': 1,
        'title': 'V for Vendetta',
        'overview': 'La venganza retorna las calles en cuerpo de un individuo que busca la justicia por mano propia',
        'year': 2005,
        'rating': 9.9,
        'category': 'Action'
    },
    {
        'id': 2,
        'title': 'Batman: Dead in the family',
        'overview': 'Batman se enfrenta a su peor villano, uno que se pensaba que había muerto',
        'year': 2020,
        'rating': 9.0,
        'category': 'Animation'
    },
    {
        'id': 3,
        'title': 'Spiderman: across the spiderverse',
        'overview': 'Miles se adentra en la aventura más descabellada de este universo y de cualquier otro en busca de como salvar a sus amigos',
        'year': 2023,
        'rating': 10.0,
        'category': 'Comedy', 
    }
]

@app.get("/", tags=["Home"])
def message():
    return HTMLResponse('<h1> Hola Mundo </h1>')



    
