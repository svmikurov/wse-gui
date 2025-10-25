"""Term Presentation API client."""

import logging

import httpx

from wse.api.glossary.responses import (
    TermPresentationResponse,
)
from wse.api.glossary.schemas import (
    TermPresentationParamsSchema,
    TermPresentationSchema,
)
from wse.config.api import APIConfigV1
from wse.core.http.auth_schema import AuthScheme

from . import TermPresentationApiABC

log = logging.getLogger(__name__)


class TermPresentationApi(TermPresentationApiABC):
    """Term Presentation API client."""

    def __init__(
        self,
        http_client: httpx.Client,
        auth_scheme: AuthScheme,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the client."""
        self._http_client = http_client
        self._auth_scheme = auth_scheme
        self._api_config = api_config

    def fetch_presentation(
        self,
        payload: TermPresentationParamsSchema,
    ) -> TermPresentationSchema | None:
        """Fetch presentation."""
        try:
            response = self._http_client.post(
                url=self._api_config.term_presentation,
                auth=self._auth_scheme,
                json=payload,
            )
            response.raise_for_status()

        except httpx.HTTPError:
            log.exception('Request Term Presentation HTTP error\n')

        else:
            if not hasattr(response, 'json'):
                log.error(
                    'Request Term Presentation error: '
                    'response does not contain JSON data\n'
                )

            else:
                try:
                    validated_data = TermPresentationResponse(
                        **response.json()
                    )

                except ValueError as err:
                    log.exception(
                        f'Term Presentation response validate error:\n'
                        f'{str(err)}\n'
                        f'Got response JSON: {response.json()}'
                    )

                else:
                    return validated_data.data

        return None
