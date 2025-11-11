"""Term API client."""

import logging

import httpx
from injector import inject
from pydantic import ValidationError

from wse.config.api import APIConfigV1
from wse.core.http.auth_schema import AuthSchema

from . import TermApiABC, responses, schemas

log = logging.getLogger(__name__)


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

    def fetch_terms(self) -> schemas.TermsData | None:
        """Fetch terms."""
        try:
            response = self._http_client.get(
                auth=self._auth_scheme,
                url=self._api_config.terms,
            )
            response.raise_for_status()

        except httpx.HTTPError:
            log.exception('Request Terms HTTP error:\n')

        else:
            if not hasattr(response, 'json'):
                log.error(
                    'Request Terms error: response does not contain JSON data'
                )

            else:
                try:
                    validated_data = responses.TermsResponse(**response.json())

                except ValidationError as err:
                    log.exception(
                        f'Terms response validate error:\n{str(err)}\n'
                        f'Got response JSON:\n{response.json()}'
                    )

                else:
                    return validated_data.data

        return None
