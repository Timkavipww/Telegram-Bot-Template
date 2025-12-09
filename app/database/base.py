from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import config

engine = create_async_engine(
    config.DATABASE_URL, 
    echo=False
)

async_session_maker: sessionmaker = sessionmaker(
    engine,
    class_= AsyncSession, 
    expire_on_commit=False
)

Base = declarative_base()