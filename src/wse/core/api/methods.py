"""Defines HTTP methods as an enumeration."""

from enum import Enum


class HTTPMethod(str, Enum):
    """Represents HTTP methods."""

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
