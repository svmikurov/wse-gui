"""Defines protocols for data storage services."""

from typing import Protocol


class JWTStorageProto(Protocol):
    """Protocol for JWT storage interface."""

    def save_tokens(self, access: str, refresh: str) -> None:
        """Save JWT tokens."""

    @property
    def access_token(self) -> str:
        """Get access storage token."""

    @access_token.setter
    def access_token(self, token: str) -> None:
        """Get access storage token."""

    @property
    def refresh_token(self) -> str:
        """Get access storage token."""

    def delete_tokens(self, missing_ok: bool = True) -> None:
        """Delete JWT tokens."""


class JWTJsonStorageProto(JWTStorageProto, Protocol):
    """Protocol for JWT storage with JSON interface."""
