from fastapi import Request
from fastapi.responses import JSONResponse


class CustomException(Exception):
    def __init__(self, status_code: int, content: dict):
        self.exception_case = self.__class__.__name__
        self.status_code = status_code
        self.content = content

    def __str__(self):
        return (
            f"<AppException {self.exception_case} - "
            + f"status_code={self.status_code} - content={self.content}>"
        )


async def custom_app_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "app_exception": exc.exception_case,
            "content": exc.content,
        },
    )


class AppException:
    class PackageNotFoundException(CustomException):
        def __init__(self, content: dict = None):
            """
            Package not found
            """
            status_code = 404
            CustomException.__init__(self, status_code, content)
