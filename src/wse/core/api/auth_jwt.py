"""Defines authentication with JWT the API service."""

import logging
from http import HTTPStatus

import httpx
from httpx import URL
from injector import inject
from typing_extensions import override

from wse.config.settings import APIConfigV1
from wse.core.exceptions import AuthError
from wse.core.interfaces.iapi import IAuthAPIjwt

logger = logging.getLogger(__name__)


class AuthAPIjwt(IAuthAPIjwt):
    """Authentication with JWT the API service."""

    @inject
    def __init__(
        self,
        http_client: httpx.Client,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the API."""
        self._http_client = http_client
        self._base_url = URL(api_config.base_url)
        # Endpoints
        self._obtain_token_endpoint = URL(api_config.jwt['obtain_token'])
        self._refresh_token_endpoint = URL(api_config.jwt['refresh_token'])
        self._check_token_endpoint = URL(api_config.jwt['check_token'])

    @override
    def obtain_tokens(self, username: str, password: str) -> dict[str, str]:
        """Obtain 'refresh' and 'access' tokens."""
        url = self._base_url.join(self._obtain_token_endpoint)

        try:
            response = self._http_client.post(
                url=url,
                json={'username': username, 'password': password},
            )
            response.raise_for_status()

        except httpx.HTTPError as e:
            logger.exception(f'HTTP Exception for {e.request.url} - {e}')
            raise AuthError from e

        else:
            tokens: dict[str, str] = response.json()
            return tokens

    def refresh_access_token(self, refresh_token: str) -> str:
        """Refresh the 'access' token."""
        headers = {'Authorization': f'Bearer {refresh_token}'}

        try:
            response = self._http_client.post(
                self._refresh_token_endpoint,
                headers=headers,
            )
            response.raise_for_status()

        except httpx.HTTPError as exc:
            logger.exception(f'HTTP Exception for {exc.request.url} - {exc}')
            raise AuthError from exc

        else:
            logger.debug(f'Success refreshed token for {self._base_url}')
            token: str = response.json()['access']
            return token

    def check_access_token(self, access_token: str) -> bool:
        """Check the access token."""
        try:
            response = self._http_client.post(
                URL('http://127.0.0.1:8000/').join(self._check_token_endpoint),
                json={'token': access_token},
            )
            response.raise_for_status()

        except httpx.HTTPStatusError as e:
            logger.error(f'Access token verification error: {e}')
            return False

        except httpx.HTTPError as e:
            logger.exception(f'Request error: {e}')
            return False

        else:
            return True if response.status_code == HTTPStatus.OK else False
