from bot.middleware.db_session_middleware import DbSessionMiddleware
from bot.middleware.service_middleware import ServiceMiddleware
from bot.middleware.ensure_user_middleware import EnsureUserMiddleware

from bot.bot import bot, dp
from app.database.init_db import init_models
from app.utils.logger import logger
from bot.handlers import router
from app.settings.config import config
import asyncio

async def main():

    await init_models()
    config.validate_config()
    
    dp.include_router(router=router)
    dp.update.middleware(DbSessionMiddleware())
    
    dp.message.middleware(EnsureUserMiddleware())
    dp.message.middleware(ServiceMiddleware())

    logger.info("[MAIN] Bot started!")
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ex:
        logger.warning(f"[MAIN] Выключен вручную\n{ex}")
    except Exception as ex:
        logger.critical(f"[MAIN] Unhandled exception\n{ex}")