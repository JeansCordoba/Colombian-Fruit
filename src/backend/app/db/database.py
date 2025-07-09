from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os
from typing import AsyncGenerator

load_dotenv()

# Create async database URL
url = URL.create(
    drivername="postgresql+asyncpg",
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=5432,
    database=os.getenv('POSTGRES_DB')
)

# Create async engine
engine = create_async_engine(
    url,
    echo=False,  # Set to True for SQL query logging
    pool_pre_ping=True,
    pool_recycle=300
)

# Create async session factory
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def create_db_and_tables():
    """Create database tables asynchronously."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get async database session."""
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
