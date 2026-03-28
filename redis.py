import redis.asyncio as redis

from settings import get_settings

settings = get_settings()

_redis_pool = redis.ConnectionPool.from_url(
    settings.redis_url.encoded_string(),
    decode_responses=True,
    max_connections=settings.redis_connections,
)

redis_client = redis.Redis(connection_pool=_redis_pool)
