from pydantic import BaseModel


class Character(BaseModel):
    name: str
    description: str
    profile_image: str

    prompt: str
    tags: list[str]

    class Config:
        from_attributes = True


class CharacterChat(BaseModel):
    chat: list[str]

    class Config:
        from_attributes = True
