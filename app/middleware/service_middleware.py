from typing import Any, Dict
from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository

from app.services.user_service import UserService

class ServiceMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(self, handler, event: Any, data: Dict[str, Any]):
        session: AsyncSession = data.get("session")
        if session:
            user_repo = UserRepository(session)
            data["user_service"] = UserService(user_repo)
        return await handler(event, data)