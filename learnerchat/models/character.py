from pydantic import BaseModel


class Character(BaseModel):
    name: str
    description: str
    profile_image: str

    prompt: str
    tags: list[str]
