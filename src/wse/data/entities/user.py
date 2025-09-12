"""The User entity of Data layer."""

from dataclasses import dataclass
from typing import TypedDict


class UserFieldType(TypedDict, total=False):
    """Field types for User data."""

    username: str
    balance: str
    is_authenticated: bool


@dataclass(frozen=True)
class User:
    """User entity."""

    username: str = 'Anonymous'
    balance: str | None = None
    is_authenticated: bool = False
