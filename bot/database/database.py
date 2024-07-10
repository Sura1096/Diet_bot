from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from ..config.config import load_config


config_data = load_config()
engine = create_async_engine(config_data.db.ASYNC_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Метатаблица, которая позволит создавать модели SQLAlchemy
class Base(DeclarativeBase):
    pass
