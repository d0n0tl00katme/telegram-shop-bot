from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = str(os.getenv("DB_URL"))

engine = create_async_engine(
    DB_URL,
)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
