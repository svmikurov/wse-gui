"""Home screen repository."""

from ..repositories.abc import HomeRepoABC
from ..sources.user import UserSourceABC


class HomeRepo(HomeRepoABC):
    """Home screen repository."""

    _user_source: UserSourceABC

    @property
    def is_authenticated(self) -> bool:
        """Refresh home screen context."""
        return self._user_source.is_authenticated
