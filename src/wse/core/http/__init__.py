"""Contains HTTP request components.

Contains:
    - HTTP client
    - Authentication schema
    - Account state inspector
"""

__all__ = [
    'IHttpClient',
]

from ._iabc.client import IHttpClient
