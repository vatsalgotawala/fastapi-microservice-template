import logging
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request

from myservice.schemas.common import HealthCheck
from myservice.schemas.common import VersionInfo
from myservice.schemas.common import VersionInfoQueryArgs
from myservice.utils.exceptions import AppException

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/healthcheck", response_model=HealthCheck)
async def health_check():
    return {"status": "up"}


@router.get("/versioninfo", response_model=VersionInfo)
async def version_info(
    request: Request, query_params: VersionInfoQueryArgs = Depends()
):
    try:
        logger.debug(
            f"trace_id({request.state.trace_id}) | Processing request {request.url.path}"
        )
        __version__ = version(query_params.package_name)
    except PackageNotFoundError:
        raise AppException.PackageNotFoundException(
            content={
                "message": "Package not found",
                "package_name": query_params.package_name,
            }
        )
    return {"version_info": __version__, "package_name": query_params.package_name}
