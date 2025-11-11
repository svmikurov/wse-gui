"""Abstract base classes for API client."""

from abc import ABC, abstractmethod


class AuthAPIjwtABC(ABC):
    """ABC for authentication API interface."""

    @abstractmethod
    def obtain_tokens(self, username: str, password: str) -> dict[str, str]:
        """Obtain 'refresh' and 'access' tokens."""

    @abstractmethod
    def check_access_token(self, access_token: str) -> bool:
        """Check the access token."""

    @abstractmethod
    def refresh_access_token(self, refresh_token: str) -> str:
        """Refresh the 'access' token."""
