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
    'LoginProto',
    'LoginObserver',
    # Protocols
    'LoginModelProto',
    'LoginContainerProto',
    'LoginControllerProto',
]

from .interface import LoginObserver, LoginProto
from .protocols import (
    LoginContainerProto,
    LoginControllerProto,
    LoginModelProto,
)
