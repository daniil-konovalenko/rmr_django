import functools

from rmr.compat import user_is_authenticated
from rmr.errors import ClientError


def authentication_required(fn):
    @functools.wraps(fn)
    def _wrapper(request, *args, **kwargs):
        if not user_is_authenticated(request.user):
            raise ClientError(
                'Authentication required',
                http_code=401,
                code='authentication_required',
            )
        return fn(request, *args, **kwargs)
    return _wrapper
