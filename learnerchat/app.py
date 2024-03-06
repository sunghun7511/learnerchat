from fastapi import FastAPI

from views import auth_router, character_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(auth_router)
    app.include_router(character_router)

    return app
