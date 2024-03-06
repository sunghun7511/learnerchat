from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from core.auth import get_current_user
from core.character import get_character_list, create_character, chat_character
from models.user import User

router = APIRouter(prefix="/character")


@router.get("/list")
async def view_get_character_list(
    current_user: Annotated[User, Depends(get_current_user)],
    page: int = 1,
    per_page: int = 20,
):
    return await get_character_list(page=page, per_page=per_page)


@router.post("/")
async def view_post_character(
    current_user: Annotated[User, Depends(get_current_user)],
    name: str,
    description: str,
    image_url: str,
    prompt: str,
    tags: list[str],
):
    return await create_character(current_user, name, description, image_url, prompt, tags)


@router.get("/{character_id}/chat", response_class=StreamingResponse)
async def view_get_character_chat(
    character_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
):
    pass
