"""Contains HTTP request components.

Contains:
    - Authentication schema
    - HTTP client
"""

__all__ = [
    'AuthSchemeProto',
    'HttpClientProto',
]

from .protocol import (
    AuthSchemeProto,
    HttpClientProto,
)
