"""HTTP-methods."""

from enum import Enum


class HTTPMethod(str, Enum):
    """HTTP-methods."""

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
