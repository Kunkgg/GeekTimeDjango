import time 
import logging

LOG = logging.getLogger(__name__)


def performance_logger_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        duration = round((time.time() - start_time) * 1000, 2)
        response['X-Page-Duration-ms'] = duration
        LOG.info(f'{duration:.2f}ms, {request.path}, {request.GET.dict()}')
        return response

    return middleware
