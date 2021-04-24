from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from myservice.config import config
from myservice.utils.helpers import camelcase


class CamelCaseModel(BaseModel):
    """
    Class for camelizing request and response bodies
    while keeping your python code snake cased.
    """

    class Config:
        alias_generator = camelcase
        allow_population_by_field_name = True


class VersionInfoQueryArgs(CamelCaseModel):
    package_name: Optional[str] = config.app_name


class VersionInfo(CamelCaseModel):
    version_info: str
    package_name: str


class HealthCheck(CamelCaseModel):
    status: str = Field("up", const=True)
