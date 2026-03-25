import asyncio

import structlog

log = structlog.get_logger()


async def main() -> None:
    while True:
        await asyncio.sleep(1)
        print("Test")


if __name__ == "__main__":
    log.info("worker.start")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("worker.stop")
    finally:
        log.info("worker.exit")
