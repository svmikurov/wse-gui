"""Defines protocol for API client interface."""

from typing import Any, Generator, Protocol

import httpx
from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core.math.rest import SimpleCalcCheck, SimpleCalcResult


class IHttpClient(Protocol):
    """Protocol for http client."""

    def get(
        self,
        url: httpx.URL | str,
        auth: httpx.Auth | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""

    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: httpx.Auth | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send a `POST` request."""

    def patch(
        self,
        url: httpx.URL | str,
        json: dict[str, Any],
        auth: httpx.Auth | None = None,
    ) -> httpx.Response:
        """Send a `PATCH` request."""


class IAuthAPIjwt(Protocol):
    """Protocol for authentication API interface."""

    def obtain_tokens(self, username: str, password: str) -> dict[str, str]:
        """Obtain 'refresh' and 'access' tokens."""

    def check_access_token(self, access_token: str) -> bool:
        """Check the access token."""

    def refresh_access_token(self, refresh_token: str) -> str:
        """Refresh the 'access' token."""


class IExerciseAPI(Protocol):
    """Defines protocol for exercise API interface."""

    def request_task(self, exercise: ExerciseEnum) -> dict[str, Any]:
        """Request the task."""

    def check_answer(self, answer: SimpleCalcCheck) -> SimpleCalcResult:
        """Check the user entered answer."""


class IAuthScheme(Protocol):
    """Protocol for authentication schema interface."""

    def auth_flow(
        self,
        request: httpx.Request,
    ) -> Generator[httpx.Request, httpx.Response, None]:
        """Execute the authentication flow."""
