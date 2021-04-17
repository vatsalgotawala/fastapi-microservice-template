import time
import uuid

from fastapi import Request

from myservice.logger import logger


async def log_timed_requests(request: Request, call_next):
    trace_id = request.headers.get("x-trace-id") or str(uuid.uuid4())
    request.state.trace_id = trace_id
    logger.debug(f"trace_id({trace_id}) | Start request {request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)
    logger.info(
        f"trace_id({trace_id}) | Request {request.url.path} "
        + f"| duration({formatted_process_time}ms) | "
        + f"response_status_code({response.status_code})"
    )

    return response
