from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from typing import Callable, Awaitable, Any, Dict

from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.utils.logger import logger

class EnsureUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Message):
            session = data.get("session")
            if session is None:
                logger.warning("[EnsureUserMiddleware] Нет session в данных мидлвари")
                return await handler(event, data)

            repo = UserRepository(session)
            service = UserService(repo)

            telegram_id = event.from_user.id
            username = event.from_user.username

            user = await service.get_user(telegram_id)

            if not user:
                await service.create_user(id=telegram_id, username=username)
                logger.info(f"[EnsureUserMiddleware] Создан новый пользователь: {telegram_id}")

        return await handler(event, data)
