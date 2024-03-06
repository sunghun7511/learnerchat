from fastapi import FastAPI

from learnerchat.core.setup import check_and_init
from learnerchat.views import auth_router, character_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(auth_router)
    app.include_router(character_router)

    @app.on_event("startup")
    async def startup():
        await check_and_init()

    return app
