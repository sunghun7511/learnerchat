from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse

from core.auth import get_current_user
from models.user import User

router = APIRouter(prefix="/character")


@router.get("/list", response_class=HTMLResponse)
async def view_get_character_list(
    current_user: Annotated[User, Depends(get_current_user)]
):
    pass
