"""Defines authentication with JWT the API service."""

import logging

import httpx
from httpx import URL
from injector import inject
from typing_extensions import override

from wse.config.api import APIConfigV1
from wse.core.exceptions import AuthError

from .abc import AuthAPIjwtABC

log = logging.getLogger(__name__)


class AuthAPIjwt(AuthAPIjwtABC):
    """Authentication with JWT the API service."""

    # Uses `httpx.Client` for sensitive data
    @inject
    def __init__(
        self,
        http_client: httpx.Client,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the API."""
        # Http Client
        self._http_client = http_client
        self._http_client.base_url = api_config.base_url

        # Endpoints
        self._obtain_token_endpoint = URL(api_config.jwt['obtain_token'])
        self._refresh_token_endpoint = URL(api_config.jwt['refresh_token'])
        self._check_token_endpoint = URL(api_config.jwt['check_token'])

    @override
    def obtain_tokens(self, username: str, password: str) -> dict[str, str]:
        """Obtain 'refresh' and 'access' tokens."""
        try:
            response = self._http_client.post(
                url=self._obtain_token_endpoint,
                json={'username': username, 'password': password},
            )
            response.raise_for_status()

        except httpx.HTTPError as e:
            log.exception(f'HTTP Exception for {e.request.url} - {e}')
            raise AuthError from e

        else:
            tokens: dict[str, str] = response.json()
            return tokens

    def check_access_token(self, access_token: str) -> bool:
        """Check the access token."""
        try:
            response = self._http_client.post(
                url=self._check_token_endpoint,
                json={'token': access_token},
            )
            response.raise_for_status()

        except httpx.ConnectError:
            log.error('Access token verification incomplete')
            return False

        except httpx.HTTPStatusError as e:
            log.error(f'Access token verification error: {e}')
            raise e

        except httpx.HTTPError as e:
            log.exception(f'Request error: {e}')
            return False

        except Exception as e:
            log.exception(f'Unknown error: {e}')
            return False

        else:
            log.info('Token verified successfully')
            return True

    def refresh_access_token(self, refresh_token: str) -> str:
        """Refresh the access token."""
        try:
            response = self._http_client.post(
                url=self._refresh_token_endpoint,
                json={'refresh': refresh_token},
            )
            response.raise_for_status()

        except httpx.HTTPError as e:
            log.exception(f'Token refresh error for {e.request.url} - {e}')
            raise e

        else:
            log.debug(f'Success refreshed token for {response.url.host}')
            token: str = response.json()['access']
            return token
