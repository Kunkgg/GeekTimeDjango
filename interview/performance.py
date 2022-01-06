import time 
import logging
import traceback

from sentry_sdk import capture_exception, capture_message
from django.http import HttpResponse


LOG = logging.getLogger(__name__)
SLOW_MS = 200


def performance_logger_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        duration = round((time.time() - start_time) * 1000, 2)
        response['X-Page-Duration-ms'] = duration
        LOG.info(f'{duration:.2f}ms, {request.path}, {request.GET.dict()}')
        return response

    return middleware


class PerformanceAndExceptionLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        start_time = time.time()
        response = self.get_response(request)
        duration = round((time.time() - start_time) * 1000, 2)
        response['X-Page-Duration-ms'] = duration
        message = f'{duration:.2f}ms, {request.path}, {request.GET.dict()}'
        LOG.info(message)
        # Code to be executed for each request/response after
        # the view is called.
        if duration > SLOW_MS:
            capture_message(f'Slow request, {message}')

        return response

    def process_exception(self, request, exception):
        if exception:
            message = "url:{url} ** msg:{error} ````{tb}````".format(
                url = request.build_absolute_uri(),
                error = repr(exception),
                tb = traceback.format_exc()
            )
            
            LOG.warning(message)
            
            # send dingtalk message
            # dingtalk.send(message)

            # capture exception to sentry:
            capture_exception(exception)
                
        return HttpResponse("Error processing the request, please contact the system administrator.", status=500)
