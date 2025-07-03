from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from .models import Base
from sqlalchemy.ext.asyncio import async_sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = str(os.getenv("DB_URL"))

engine = create_async_engine(
    DB_URL,
)

SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
