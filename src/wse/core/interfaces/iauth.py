"""Defines protocol fir Authenticate service interface."""

from typing import Protocol


class IAuthService(
    Protocol,
):
    """Protocol for Authenticate service interface."""

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate the user."""
