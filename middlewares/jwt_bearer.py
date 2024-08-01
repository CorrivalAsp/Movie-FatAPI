from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials 
from fastapi import Request, HTTPException
from utils.jwtmanager import valide_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth: HTTPAuthorizationCredentials = await super().__call__(request)
        token = auth.credentials
        try:
            data = valide_token(token)
        except Exception as e:
            raise HTTPException(status_code=403, detail='Token inválido o ha expirado')
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail='Credenciales inválidas')