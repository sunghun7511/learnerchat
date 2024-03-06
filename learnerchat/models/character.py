from pydantic import BaseModel


class Character(BaseModel):
    name: str
    description: str
    image_url: str

    prompt: str
    tags: str

    class Config:
        from_attributes = True


class CharacterChat(BaseModel):
    chat: list[str]

    class Config:
        from_attributes = True
