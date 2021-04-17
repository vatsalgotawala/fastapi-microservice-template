from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from myservice.config import config


# function to convert a snake case string into a camel case
def camelcase(input_string):
    parts = iter(input_string.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


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
