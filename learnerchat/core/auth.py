from typing import Annotated

from decouple import config
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import encode, decode

from models.user import User

JWT_SECRET = config("JWT_SECRET", "SampleSecret")

security = HTTPBearer()
users = dict()


def create_jwt_token(email: str) -> str:
    return encode({"email": email}, JWT_SECRET, algorithm="HS256")


async def get_current_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> User:
    email = decode(credentials.credentials, JWT_SECRET, algorithms=["HS256"]).get("email", "")
    if email not in users:
        raise ValueError("User not found")

    return users[email]


async def register(email: str, nickname: str) -> str:
    if email in users:
        raise ValueError("User already exists")

    users[email] = User(email=email, nickname=nickname)
    return create_jwt_token(email)


async def login(email: str) -> str:
    user = None
    return create_jwt_token(email)
