from typing import Any, Dict
from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository

from app.services.user_service import UserService

class ServiceMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Any, data: Dict[str, Any]):
        session: AsyncSession | None = data.get("session")

        if session is not None:
            data["user_service"] = UserService(UserRepository(session))

        return await handler(event, data)