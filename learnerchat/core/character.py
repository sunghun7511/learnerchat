from sqlalchemy.future import select

from learnerchat.models.user import User
from learnerchat.models.character import Character
from learnerchat.models.dao import CharacterDAO

from learnerchat.database import session


async def get_character_list(*, page: int = 1, per_page: int = 20) -> list[Character]:
    query = select(CharacterDAO).limit(per_page).offset((page - 1) * per_page)
    result = await session.execute(query)
    return [Character.from_orm(character) for character in result.all()]


async def create_character(
    user: User,
    name: str,
    description: str,
    image_url: str,
    prompt: str,
    tags: list[str]
) -> Character:
    character = CharacterDAO(
        user_id=user.id,
        name=name,
        description=description,
        image_url=image_url,
        prompt=prompt,
        tags=",".join(tags)
    )
    session.add(character)
    await session.commit()
    return Character.from_orm(character)


async def chat_character():
    pass
