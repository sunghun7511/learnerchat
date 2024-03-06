from typing import Annotated

from decouple import config
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import encode, decode

from models.user import User

JWT_SECRET = config("JWT_SECRET", "SampleSecret")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    user: dict = decode(token, JWT_SECRET, algorithms=["HS256"])
    return User(**user)


async def register(email: str, nickname: str):
    pass


async def login(email: str) -> str:
    user = None
    nickname = ""

    return encode({"email": email, "nickname": nickname}, JWT_SECRET, algorithm="HS256")
