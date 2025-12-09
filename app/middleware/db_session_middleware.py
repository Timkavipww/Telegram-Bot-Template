from typing import Any, Dict
from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession #noqa
from app.database.base import async_session_maker

class DbSessionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Any, data: Dict[str, Any]):
        async with async_session_maker() as session:
            data["session"] = session
            return await handler(event, data)