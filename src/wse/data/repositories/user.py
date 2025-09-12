"""User data repository."""

from abc import ABC, abstractmethod

from injector import inject

from ..sources.user import UserSource


class UserRepoABC(ABC):
    """ABC for User data repository."""

    @abstractmethod
    def update_balance(self, balance: str) -> None:
        """Update user balance."""


class UserRepo:
    """User data repository."""

    @inject
    def __init__(
        self,
        user_source: UserSource,
    ) -> None:
        """Construct the repository."""
        self._user_source = user_source

    def update_balance(self, balance: str) -> None:
        """Update user balance."""
        self._user_source.update_balance(balance)
