"""Service interfaces."""

# ruff: noqa: D101, D102

from typing import Protocol


class IAuthService(Protocol):
    def is_authenticated(self) -> bool: ...
