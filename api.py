import json
import uuid
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import stream

import structlog
from fastapi import FastAPI
from fastapi.responses import Response
from starlette.status import HTTP_202_ACCEPTED

from settings import get_settings

settings = get_settings()
log = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    log.info("lifespan.startup")
    yield
    log.info("lifespan.shutdown")


app = FastAPI(lifespan=lifespan)


@app.post("/curriculum")
async def root(curriculum: str):




# @app.get("/curriculum/status/{curriculum_id}")
# async def status(curriculum_id: str):
#     result = r.xpending("curriculums", curriculum_id)
#     print(result)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
