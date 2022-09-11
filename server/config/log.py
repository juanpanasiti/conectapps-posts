import time
from datetime import datetime
from pydantic import BaseModel
from fastapi.routing import APIRoute
from typing import Callable
from fastapi import Request, Response

import logging

logger = logging.getLogger()


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "mycoolapp"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = True
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "mycoolapp": {"handlers": ["default"], "level": LOG_LEVEL},
    }


class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            date = datetime.now().strftime('%Y-%m-%d %X')
            req_data = f'[{request.method}] {request.url.path}?{request.url.query}'
            response: Response = await original_route_handler(request)
            duration = (time.time() - before) * 1000
            res_data = f'{response.status_code} - {round(duration,3)}ms'
            msg_log = f'{date} - "{req_data}" - {res_data}'
            logger.info(msg_log)
            return response

        return custom_route_handler
