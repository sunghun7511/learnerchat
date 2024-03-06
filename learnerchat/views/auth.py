from core.auth import register, login
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.post("/register", response_class=HTMLResponse)
async def view_post_register(request: Request):
    pass


@router.post("/login", response_class=HTMLResponse)
async def view_post_login(request: Request):
    pass
