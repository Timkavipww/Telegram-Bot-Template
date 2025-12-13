from aiogram import Router

from bot.handlers.start_handler import router as start_router
from bot.handlers.admin_handler import router as admin_router
from bot.middleware.admin_middleware import AdminMiddleware
router = Router()

admin_router.message.middleware(AdminMiddleware())

router.include_router(admin_router)
router.include_router(start_router)