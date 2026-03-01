"""Consistent error response formatting."""

from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse


class APIException(HTTPException):
    """Base API exception with consistent error format."""

    def __init__(self, status_code: int, detail: str, error_code: str | None = None):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code


async def api_exception_handler(request: Request, exc: APIException) -> JSONResponse:
    """Handle API exceptions with consistent format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.error_code or "API_ERROR",
                "message": exc.detail,
                "status": exc.status_code,
            }
        },
    )


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """Handle HTTP exceptions with consistent format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"code": "HTTP_ERROR", "message": exc.detail, "status": exc.status_code}},
    )


async def validation_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle validation exceptions from Pydantic."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Validation failed",
                "status": 422,
                "details": str(exc),
            }
        },
    )
