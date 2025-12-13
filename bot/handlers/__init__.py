from aiogram import Router

from bot.handlers.start_handler import router as start_router

router = Router()

router.include_router(start_router)