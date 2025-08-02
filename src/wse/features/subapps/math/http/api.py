"""Defines API for context requests."""

from typing import Any

from injector import inject
from typing_extensions import override

from wse.core.http import IHttpClient
from wse.core.interfaces.iapi import IAuthScheme

from ._iabc import MathAPIABC
from .config import MathAPIConfigV1


class MathAPI(MathAPIABC):
    """API for math app."""

    @inject
    def __init__(
        self,
        http_client: IHttpClient,
        auth_scheme: IAuthScheme,
        api_config: MathAPIConfigV1,
    ) -> None:
        """Construct the api."""
        self._http_client = http_client
        self._auth_scheme = auth_scheme
        self._api_config = api_config

    @override
    def get_index_context(self) -> dict[str, Any]:
        """Get context for index page context."""
        response = self._http_client.get(
            self._api_config.index,
        )
        data: dict[str, Any] = response.json()
        return data
