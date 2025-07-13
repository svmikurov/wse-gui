"""Defines authentication scheme."""

import logging
from http import HTTPStatus

import httpx
from httpcore import Request
from httpx import Response
from injector import inject
from typing_extensions import Generator, override

from wse.core.interfaces.iapi import IAuthScheme
from wse.core.interfaces.iauth import IAuthService

logger = logging.getLogger(__name__)


class AuthSchema(httpx.Auth, IAuthScheme):
    """Custom authentication schema.

    Use with httpx.Client for authenticated request.
    """

    @inject
    def __init__(
        self,
        auth_service: IAuthService,
    ) -> None:
        """Construct the sschema."""
        self._auth_service = auth_service

    @override
    def auth_flow(  # type: ignore[override]
        self,
        request: Request,
    ) -> Generator[Request, Response, None]:
        """Execute the authentication flow."""
        if self._auth_service.is_auth:
            request = self._add_auth_header(request)

        response = yield request

        if response.status_code == HTTPStatus.UNAUTHORIZED:
            # If the server issues a 401 response, then issue a
            # request to refresh tokens, and resend the request.
            self._auth_service.refresh_access_token()
            request = self._add_auth_header(request)
            yield request

    def _add_auth_header(self, request: Request) -> Request:
        """Add authentication with JWT to request header."""
        request.headers['Authorization'] = (  # type: ignore[call-overload]
            f'Bearer {self._auth_service.access_token}'
        )
        return request
