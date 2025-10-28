"""Term API client."""

import logging

import httpx
from injector import inject
from pydantic import ValidationError

from wse.api.glossary.abc import TermApiABC
from wse.api.glossary.responses import TermsResponse
from wse.api.glossary.schemas import TermsData
from wse.config.api import APIConfigV1
from wse.core.http.auth_schema import AuthSchema

logger = logging.getLogger(__name__)


class TermApi(TermApiABC):
    """Term API client."""

    @inject
    def __init__(
        self,
        http_client: httpx.Client,
        auth_scheme: AuthSchema,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the client."""
        self._http_client = http_client
        self._auth_scheme = auth_scheme
        self._api_config = api_config

    def fetch_terms(self) -> TermsData | None:
        """Fetch terms."""
        try:
            response = self._http_client.get(
                auth=self._auth_scheme,
                url=self._api_config.terms,
            )
            response.raise_for_status()

        except httpx.HTTPError:
            logger.exception('Request Terms HTTP error:\n')

        else:
            if not hasattr(response, 'json'):
                logger.error(
                    'Request Terms error: response does not contain JSON data'
                )

            else:
                try:
                    validated_data = TermsResponse(**response.json())

                except ValidationError as err:
                    logger.exception(
                        f'Terms response validate error:\n{str(err)}\n'
                        f'Got response JSON:\n{response.json()}'
                    )

                else:
                    return validated_data.data

        return None
