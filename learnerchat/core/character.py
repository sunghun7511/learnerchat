from sqlalchemy.future import select

from models.user import User
from models.character import Character
from models.dao import CharacterDAO

from database import session


async def get_character_list(*, page: int = 1, per_page: int = 20) -> list[Character]:
    query = select(CharacterDAO).limit(per_page).offset((page - 1) * per_page)
    result = await session.execute(query)
    return [Character.from_orm(character) for character in result.all()]


def create_character(
    user: User,
    name: str,
    description: str,
    image_url: str,
    prompt: str,
    tags: list[str]
):
    pass


def chat_character():
    pass
