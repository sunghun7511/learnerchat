from typing import Annotated

from decouple import config
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import encode, decode
from sqlalchemy.future import select

from models.user import User
from models.dao import UserDAO

from database import session

JWT_SECRET = config("JWT_SECRET", "SampleSecret")

security = HTTPBearer()


def create_jwt_token(email: str) -> str:
    return encode({"email": email}, JWT_SECRET, algorithm="HS256")


async def get_current_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> User:
    email = decode(credentials.credentials, JWT_SECRET, algorithms=["HS256"]).get("email", "")

    query = select(UserDAO).where(UserDAO.email == email)
    result = await session.execute(query)
    users = result.scalars().all()
    if len(users) == 0:
        raise ValueError("User not found")

    return User.from_orm(users[0])


async def register(email: str, nickname: str) -> str:
    query = select(UserDAO).where(UserDAO.email == email)
    result = await session.execute(query)
    users = result.scalars().all()
    if len(users) != 0:
        raise ValueError("User already exists")

    session.add(UserDAO(email=email, nickname=nickname))
    await session.commit()

    return create_jwt_token(email)


async def login(email: str) -> str:
    query = select(UserDAO).where(UserDAO.email == email)
    result = await session.execute(query)
    users = result.scalars().all()
    if len(users) == 0:
        raise ValueError("User not found")

    return create_jwt_token(email)
