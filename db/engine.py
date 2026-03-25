"""engine.py"""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

engine = create_async_engine(
    "postgresql+asyncpg://user:pwd@5432/asyncio",
    pool_size=20,
    max_overflow=10,
    pool_timeout=30,
    echo=False,
)

AsyncSessionFactory = async_sessionmaker(engine, expire_on_commit=False)
