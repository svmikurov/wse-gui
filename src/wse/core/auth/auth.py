"""Authentication service."""

from wse.interfaces.iservices import IAuthService


class AuthService(IAuthService):
    """Authentication service."""

    def __init__(self) -> None:
        """Construct the service."""

    def is_authenticated(self) -> bool:
        """Is authenticated user."""
        return True
