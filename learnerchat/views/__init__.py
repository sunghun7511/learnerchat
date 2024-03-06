from .auth import router as auth_router
from .character import router as character_router

__all__ = [
    "auth_router",
    "character_router",
]
