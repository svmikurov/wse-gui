"""Repository for related HTTP response data."""

from abc import ABC, abstractmethod

from injector import inject

from wse.core.api.response import RelatedData
from wse.data.repositories.user import UserRepo


class RelatedDataHttpResponseRepoABC(ABC):
    """ABC for repository of related HTTP response data."""

    @abstractmethod
    def update_related(self, data: RelatedData) -> None:
        """Update the related HTTP response data."""


class RelatedDataHttpResponseRepo(
    RelatedDataHttpResponseRepoABC,
):
    """Repository for related HTTP response data."""

    @inject
    def __init__(
        self,
        user_repo: UserRepo,
    ) -> None:
        """Construct the repo."""
        self._user_repo = user_repo

    def update_related(self, data: RelatedData) -> None:
        """Update the related HTTP response data."""
        if data.balance is not None:
            self._user_repo.update_balance(data.balance)
