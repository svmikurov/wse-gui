"""Multiplication exercise controller."""

import toga
from toga.sources import Source

from wse.contrib.http_requests import request_get_async


class Task:
    """Multiplication task."""

    def __init__(self, question: str) -> None:
        """Construct the task."""
        self.question = question


class MultiplicationController(Source):
    """Multiplication exercise controller."""

    def __init__(self) -> None:
        """Construct ht controller."""
        super().__init__()
        self._task: Task | None = None

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        pass

    #####################################################################
    # Exercise methods

    def _display_question(self) -> None:
        pass

    #####################################################################
    # Button handlers

    def submit_handler(self, _: toga.Widget) -> None:
        """Submit answer, button handler."""
        pass

    #####################################################################
    # HTTP requests

    async def _request_task(self, url: str) -> None:
        response = await request_get_async(url)
        json_data = response.json()
        question = json_data['question']
        self._task = Task(question)
