"""Application core data API client."""

import logging
from abc import ABC, abstractmethod
from typing import Type, TypeVar

import httpx
from injector import inject
from pydantic import ValidationError
from typing_extensions import override

from wse.config.api import APIConfigV1
from wse.core.http.auth_schema import AuthSchema

from ..responses import InitialDataResponse

log = logging.getLogger(__name__)

T = TypeVar('T')


class DataApiABC(ABC):
    """ABC for core application data API client."""

    @abstractmethod
    def fetch_initial_data(self) -> InitialDataResponse | None:
        """Fetch initial app data."""

    @staticmethod
    def _parse_response(
        response: httpx.Response,
        response_schema: Type[T],
    ) -> T | None:
        try:
            return response_schema(**response.json())

        except ValidationError:
            log.exception(
                f'Validation error parsing API response: {response.json()}'
            )
            return None

        except (ValueError, TypeError):
            log.exception('Parsing JSON error')
            return None


class DataApi(DataApiABC):
    """Core application data API client."""

    @inject
    def __init__(
        self,
        http_client: httpx.Client,
        auth_scheme: AuthSchema,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the api."""
        self._http_client = http_client
        self._auth_scheme = auth_scheme
        self._api_config = api_config

    @override
    def fetch_initial_data(self) -> InitialDataResponse | None:
        """Fetch initial app data."""
        url_path = self._api_config.initial_data_path

        if url_path is None:
            log.error('Error load app initial data: url path not set')
            return None

        try:
            response: httpx.Response = self._http_client.get(
                auth=self._auth_scheme,
                url=url_path,
            )
            response.raise_for_status()

        except httpx.HTTPError as err:
            log.error(f'Error load app initial data: {err.args}')
            return None

        return self._parse_response(response, InitialDataResponse)
