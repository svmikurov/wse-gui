"""Defines protocol for API client interface."""

from typing import Any, AsyncGenerator, Generator, Protocol

import httpx
from httpx import Request, Response

from wse.apps.math.pages.simple_calc.dto import CalcAnswerDTO, CalcResultDTO


class IAuthAPIjwt(Protocol):
    """Protocol for authentication API interface."""

    def obtain_tokens(self, username: str, password: str) -> dict[str, str]:
        """Obtain 'refresh' and 'access' tokens."""

    def check_access_token(self, access_token: str) -> bool:
        """Check the access token."""

    def refresh_access_token(self, refresh_token: str) -> str:
        """Refresh the 'access' token."""


class IExerciseApiClient(Protocol):
    """Defines protocol for exercise API client interface."""

    def request_task(self, data: dict[str, Any]) -> dict[str, Any]:
        """Request a task from the server."""

    def check_answer(self, answer: CalcAnswerDTO) -> CalcResultDTO:
        """Check the user's entered answer on the server."""


class IAuthScheme(Protocol):
    """Protocol for authentication schema interface."""

    def auth_flow(
        self,
        request: httpx.Request,
    ) -> Generator[httpx.Request, httpx.Response, None]:
        """Execute the authentication flow."""

    def sync_auth_flow(
        self,
        request: Request,
    ) -> Generator[Request, Response, None]:
        """Execute the authentication flow synchronously."""

    async def async_auth_flow(
        self,
        request: Request,
    ) -> AsyncGenerator[Request, Response]:
        """Execute the authentication flow asynchronously."""
