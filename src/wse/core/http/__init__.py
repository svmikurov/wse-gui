"""Contains HTTP request components.

Contains:
    - Authentication schema
    - HTTP client
"""

__all__ = [
    'AuthSchemaABC',
    'HttpClientABC',
]

from .abc import (
    AuthSchemaABC,
    HttpClientABC,
)
