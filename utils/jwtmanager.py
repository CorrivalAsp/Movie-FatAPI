import jwt
from jwt import encode, decode

def create_token(data: dict):
    token : str=encode(payload=data, key="Dragon123%", algorithm="HS256")
    return token

def valide_token(token:str)-> dict: 
    data: dict=decode(token, key="Dragon123%", algorithms=['HS256'])
    return data