"""Defines protocol for API client interface."""

from typing import Any, Generator, Protocol

import httpx
from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core.math.rest import SimpleCalcCheck, SimpleCalcResult


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

    def request_task(self, data: dict[str, Any]) -> dict[str, Any]:
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
