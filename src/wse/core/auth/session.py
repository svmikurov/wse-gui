"""Defines session manager."""

from wse.interface.icore import IUser


class SessionManager:
    """Session manager."""

    def __init__(self) -> None:
        """Construct the manager."""
        self._current_user = None
        self._token = None

    def start_session(self, user: IUser, token: str) -> None:
        """Start session."""
        self._current_user = user
        self._token = token

    def end_session(self) -> None:
        """End session."""
        self._current_user = None
        self._token = None

    def is_authenticated(self) -> bool:
        """Is the user authenticated."""
        return self._current_user is not None
