from aiogram import Router

from app.handlers.start_handler import router as start_router

router = Router()

router.include_router(start_router)