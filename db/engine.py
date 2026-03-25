"""engine.py"""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from settings import get_settings

settings = get_settings()

engine = create_async_engine(
    f"postgresql+asyncpg://{settings.db_user}:{settings.db_password}@5432/{settings.db}",
    pool_size=20,
    max_overflow=10,
    pool_timeout=30,
    echo=False,
)

AsyncSessionFactory = async_sessionmaker(engine, expire_on_commit=False)
