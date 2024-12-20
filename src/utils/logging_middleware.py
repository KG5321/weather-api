import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response



class LoggingMiddleware(BaseHTTPMiddleware):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    async def dispatch(self, request: Request, call_next):
        self.logger.info(f"Request: {request.method} {request.url}")
        response: Response = await call_next(request)
        return response
