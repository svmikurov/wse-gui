"""Authentication scheme for authenticated requests.

Add authentication scheme instance to request method or constructor
of ``httpx.Client()`` to send authenticated request.

.. code-block:: python

   import httpx

   response = httpx.Client(auth=auth_scheme).get(url)

.. seealso::

   For more information, see the documentation:
   `HTTPX Authentication <https://www.python-httpx.org/advanced/authentication/>`_

"""

import logging
from http import HTTPStatus

import httpx
from httpcore import Request
from httpx import Response
from injector import inject
from typing_extensions import Generator, override

from wse.core.auth import AuthServiceProto

from .abc import AuthSchemaABC

logger = logging.getLogger(__name__)


# TODO: Fix typing ignore
class AuthSchema(httpx.Auth, AuthSchemaABC):  # type: ignore[misc]
    """Custom authentication schema.

    Use with httpx.Client() for authenticated request.

    :ivar IAuthService auth_service: Authentication service

    For example:

    .. code-block:: python

        from injector import inject

        class ApiService:

            @inject
            def __init__(
                self,
                http_client: IHttpClient,
                auth_schema: IAuthScheme,
                url: str,
            ):
                self._http_client = http_client
                self._auth_schema = auth_schema
                self._url = url

        def request_bar(self) -> httpx.Response:
            return self._http_client.get(
                url=self._url,
                auth=self._auth_scheme,
            )
    """

    @inject
    def __init__(
        self,
        auth_service: AuthServiceProto,
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
            try:
                self._auth_service.refresh_access_token()
            except Exception as e:
                logger.error('Refresh access token error')
                raise e
            else:
                request = self._add_auth_header(request)
                yield request

    def _add_auth_header(self, request: Request) -> Request:
        """Add authentication with JWT to request header."""
        request.headers['Authorization'] = (  # type: ignore[call-overload]
            f'Bearer {self._auth_service.access_token}'
        )
        return request
