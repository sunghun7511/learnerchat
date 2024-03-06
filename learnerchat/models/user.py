from pydantic import BaseModel


class User(BaseModel):
    email: str
    nickname: str

    class Config:
        from_attributes = True
