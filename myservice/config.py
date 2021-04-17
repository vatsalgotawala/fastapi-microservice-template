from enum import Enum

from pydantic import BaseSettings


class LogLevelEnum(str, Enum):
    debug = "debug"
    info = "info"


class Settings(BaseSettings):
    app_name: str = "myservice"  # TODO: Update the name of the service
    app_title: str = "My Service Title"  # TODO: Update the title of the service
    app_description: str = "Describe the purpose of this service here."  # TODO: Update the description of the service
    app_version: str = "v1"
    openapi_prefix: str = f"/{app_name}/api/{app_version}"
    openapi_url: str = "/docs/openapi.json"
    swagger_docs_url: str = f"/{app_name}/api/{app_version}/docs"
    log_level: LogLevelEnum = LogLevelEnum.info


config = Settings()
