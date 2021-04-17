import uvicorn
from fastapi import FastAPI
from fastapi import Request

from myservice.config import config
from myservice.logger import logger
from myservice.routers import ROUTERS
from myservice.utils.exceptions import custom_app_exception_handler
from myservice.utils.exceptions import CustomException
from myservice.utils.middlewares import log_timed_requests

app = FastAPI(
    title=config.app_title,
    description=config.app_description,
    version=config.app_version,
    openapi_url=config.openapi_url,
    docs_url=config.swagger_docs_url,
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    return await log_timed_requests(request, call_next)


@app.exception_handler(CustomException)
async def custom_exception_handler(request, e):
    return await custom_app_exception_handler(request, e)


logger.info("Starting APP")

for r in ROUTERS:
    app.include_router(
        r,
        prefix=(
            f"{config.openapi_prefix}{r.prefix}" if r.prefix else config.openapi_prefix
        ),
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
