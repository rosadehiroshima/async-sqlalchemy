from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db: str = "async"
    db_user: str = "admin"
    db_password: str = "password"

    @property
    def postgres_url(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.db_user,
            password=self.db_password,
            host="localhost",
            port=5432,
            path=self.db,
        )

    redis_url: str = "redis://localhost:6379/0"


def get_settings() -> Settings:
    return Settings()
