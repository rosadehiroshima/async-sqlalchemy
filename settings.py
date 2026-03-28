from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # database
    db: str = "async"
    db_user: str = "admin"
    db_password: str = "password"

    # database connection
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

    # redis
    scheme: str = "redis"
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_connections: int = 10

    @property
    def redis_url(self) -> RedisDsn:
        return RedisDsn.build(
            scheme=self.scheme,
            host=self.redis_host,
            port=self.redis_port,
            path=f"/{self.redis_db}",
        )

    # stream
    stream_name: str = ""
    group_name: str = ""
    consumer_name: str = ""

    # stream performance
    max_len: int = 1000
    batch_size: int = 100
    block_ms: int = 1000


def get_settings() -> Settings:
    return Settings()
