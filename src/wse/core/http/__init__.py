"""Contains HTTP request components.

Contains:
    - Authentication schema
    - HTTP client
"""

__all__ = [
    'AuthSchemaProto',
    'HttpClientProto',
]

from .protocol import (
    AuthSchemaProto,
    HttpClientProto,
)
