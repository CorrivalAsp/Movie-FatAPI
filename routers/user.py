
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.jwtmanager import create_token
from schemas.user import User
user_router = APIRouter()


    

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == 'admin@gmail.com' and user.passw == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content={"token": token})
    raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")