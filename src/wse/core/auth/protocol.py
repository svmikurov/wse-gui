"""Defines protocol fir Authenticate service interface."""

from typing import Protocol


class AuthServiceProto(Protocol):
    """Protocol for Authenticate service interface."""

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate the user."""

    @property
    def is_auth(self) -> bool:
        """Get user authentication state."""

    @property
    def access_token(self) -> str:
        """Get access token."""

    def logout(self) -> None:
        """Logout."""

    def set_auth_status(self) -> None:
        """Set user authenticated status."""

    def refresh_access_token(self) -> None:
        """Refresh access token."""

    def update_tokens(self, access: str, refresh: str) -> None:
        """Update tokens."""
