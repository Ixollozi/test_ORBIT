from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import async_sessionmaker, declarative_base
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL)
SessionLocal = async_sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session

