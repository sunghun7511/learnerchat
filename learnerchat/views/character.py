from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from core.auth import get_current_user
from models.user import User

router = APIRouter(prefix="/character")


@router.get("/list")
async def view_get_character_list(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return {
        "characters": [
            {
                "name": "캐릭터1",
                "description": "캐릭터1 설명",
                "profile_image": "캐릭터1 이미지",
                "prompt": "캐릭터1 프롬프트",
                "tags": ["캐릭터1 태그1", "캐릭터1 태그2"],
            }
        ]
    }


@router.post("/")
async def view_post_character(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return {"status": "ok"}


@router.get("/{character_id}/chat", response_class=StreamingResponse)
async def view_get_character_chat(
    character_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
):
    pass
