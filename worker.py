import asyncio

import structlog
from redis import Redis

from settings import get_settings

settings = get_settings()

log = structlog.get_logger()

r = Redis.from_url(settings.redis_url)


async def main() -> None:
    while True:
        await asyncio.sleep(1)
        print(r.ping())


if __name__ == "__main__":
    log.info("worker.start")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("worker.stop")
    finally:
        log.info("worker.exit")
