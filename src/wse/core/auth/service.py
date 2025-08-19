"""Defines authentication service."""

import logging

import httpx
from injector import inject
from typing_extensions import override

from wse.core.exceptions import AuthError
from wse.core.interfaces.iapi import IAuthAPIjwt
from wse.core.interfaces.iauth import IAuthService
from wse.core.interfaces.istorage import IJWTJsonStorage

logger = logging.getLogger(__name__)


class AuthService(IAuthService):
    """Authentication service."""

    @inject
    def __init__(
        self,
        auth_api: IAuthAPIjwt,
        token_storage: IJWTJsonStorage,
    ) -> None:
        """Construct the service."""
        self._auth_api = auth_api
        self._token_storage = token_storage
        self._is_auth = False

    @override
    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate the user."""
        logger.info(f"Attempting to login with '{username}' username")

        try:
            tokens: dict[str, str] = self._auth_api.obtain_tokens(
                username, password
            )
            access_token: str = tokens['access']
            refresh_token: str = tokens['refresh']

        except AuthError as e:
            logger.exception(f'Authentication error: {e}')
            self._is_auth = False
            return False

        else:
            logger.info(f"Success authentication for '{username}'")
            self.update_tokens(access_token, refresh_token)
            self._is_auth = True
            return self._is_auth

    @override
    def logout(self) -> None:
        """Logout."""
        self._token_storage.delete_tokens()
        self._is_auth = False

    @override
    @property
    def is_auth(self) -> bool:
        """Get user authentication state."""
        return self._is_auth

    def set_auth_status(self) -> None:
        """Set user authenticated status."""
        try:
            is_auth = self._auth_api.check_access_token(
                self.access_token,
            )

        except FileNotFoundError:
            self._is_auth = False

        except httpx.HTTPStatusError:
            try:
                updated_access_token = self._auth_api.refresh_access_token(
                    self._token_storage.refresh_token
                )
            except httpx.HTTPError:
                self._is_auth = False
            else:
                self._token_storage.access_token = updated_access_token
                self._is_auth = True

        except Exception:
            logger.error('Error setting authenticated status')
            raise

        else:
            self._is_auth = is_auth

    @override
    @property
    def access_token(self) -> str:
        """Get access token."""
        return self._token_storage.access_token

    def _set_access_token(self, access: str) -> None:
        self._token_storage.access_token = access

    def refresh_access_token(self) -> None:
        """Refresh access token."""
        try:
            updated_access_token = self._auth_api.refresh_access_token(
                self._token_storage.refresh_token
            )
        except Exception as e:
            raise e
        else:
            self._token_storage.access_token = updated_access_token

    def update_tokens(self, access: str, refresh: str) -> None:
        """Update tokens."""
        self._token_storage.save_tokens(access, refresh)
