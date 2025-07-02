"""Defines exercise api."""

from typing import Any

import httpx
from httpx import URL, Response
from injector import inject
from wse_exercises.core.mathem.enums import Exercises


@inject
class ExerciseApi:
    """Defines protocol for exercise API."""

    def __init__(
        self,
        http_client: httpx.Client,
    ) -> None:
        """Construct the API."""
        self._http_client = http_client
        self._base_url = URL('http://127.0.0.1:8000')
        self._exercise_endpoint = URL('/api/v1/math/calculation/simple/')

    def request_task(self, exercise: Exercises) -> dict[str, Any]:
        """Request the task."""
        data = {
            'name': exercise,
            'config': {'min_value': '1', 'max_value': '9'},
        }
        response: Response = self._http_client.post(
            self._base_url.join(self._exercise_endpoint),
            json=data,
        )
        task_data: dict[str, Any] = response.json()
        return task_data
