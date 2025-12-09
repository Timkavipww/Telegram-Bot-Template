from app.database.base import engine, Base
from app.utils.logger import logger

async def init_models():
    try:
        logger.info("[Database] Trying to initialising models")
        logger.info(f"[Database] Tables in metadata: {list(Base.metadata.tables.keys())}")
        
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            
        logger.info("[Database] Successfully initial models")
        
    except Exception as e:
        logger.error(f"[Database] fail to init models: {e}")
        raise