import functools
import requests


class RequestsWrapper(object):
    def __getattr__(self, attr):
        func = getattr(requests, attr)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, requests.models.Response):
                result.raise_for_status()
            return result
        return wrapper


requests_wrapper = RequestsWrapper()
