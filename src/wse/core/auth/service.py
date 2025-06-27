"""Defines authentication service."""

import logging

logger = logging.getLogger(__name__)


class AuthService:
    """Authentication service."""

    def __init__(self) -> None:
        """Construct the service."""

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate the user."""
        logger.info(f"Attempting to login with '{username}' username")
        return True
