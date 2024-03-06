from core.auth import register, login
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.post("/register")
async def view_post_register(email: str, nickname: str):
    token = await register(email, nickname)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login")
async def view_post_login(email: str):
    token = await login(email)
    return {"access_token": token, "token_type": "bearer"}
