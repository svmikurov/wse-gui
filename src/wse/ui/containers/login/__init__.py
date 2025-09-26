"""Authentication login feature implementation.

This module provides a complete login functionality including:
    - Credential input fields (username/password)
    - Authentication mechanism
    - UI container management
    - HTTP authentication requests

Interface:
    - clear the entered credential
    - notification about success authentication
"""

__all__ = [
    # Interface
    'LoginABC',
    'LoginObserver',
    # Protocols
    'LoginModelABC',
    'LoginContainerABC',
    'LoginControllerProto',
]

from .interface import LoginABC, LoginObserver
from .protocols import (
    LoginContainerABC,
    LoginControllerProto,
    LoginModelABC,
)
