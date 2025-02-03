"""Multiplication exercise controller."""

import json
from urllib.parse import urljoin

import toga
from toga.sources import Source

from wse.constants import HOST, MATHEMATICS_MULTIPLICATION_PATH
from wse.contrib.http_requests import request_get_async, request_post_async


class Task:
    """Multiplication task."""

    def __init__(self, data: dict) -> None:
        """Construct the task."""
        self.question = data['question']
        self.answer = data['answer']


class MultiplicationController(Source):
    """Multiplication exercise controller."""

    def __init__(self) -> None:
        """Construct ht controller."""
        super().__init__()
        self.url = urljoin(HOST, MATHEMATICS_MULTIPLICATION_PATH)
        self._task: Task | None = None
        self._user_answer: str | None = None

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        await self._start_new_task()

    #####################################################################
    # Exercise methods

    async def _start_new_task(self) -> None:
        data = await self._request_task(self.url)
        self._save_task_data(data)
        self._display_question()

    def _save_task_data(self, data: dict) -> None:
        self._task = Task(data)

    async def _check_answer(self) -> None:
        if self.user_answer == self._task.answer:
            text_result = 'Верно!'
            await self._start_new_task()
        else:
            text_result = 'Не верно!'

        self._display_result(text_result)

    @property
    def user_answer(self) -> str:
        """User answer."""
        return self._user_answer

    @user_answer.setter
    def user_answer(self, value: str) -> None:
        self._user_answer = value

    #####################################################################
    # Notifications

    def _display_question(self) -> None:
        self.notify('display_question', text=self._task.question)

    def _display_result(self, text: str) -> None:
        self.notify('display_result', text=text)

    #####################################################################
    # Widget callback functions

    async def submit_handler(self, _: toga.Widget) -> None:
        """Submit answer, button handler."""
        await self._check_answer()
        # The user's answer is stored.
        await self._sent_answer(self.url, self.user_answer)

    def update_value(self, widget: toga.MultilineTextInput) -> None:
        """Set the current user answer."""
        self.user_answer = widget.value

    #####################################################################
    # HTTP requests

    @staticmethod
    async def _request_task(url: str) -> dict:
        response = await request_get_async(url)
        return response.json()

    @staticmethod
    async def _sent_answer(url: str, user_answer: str) -> None:
        payload = {'answer': user_answer}
        await request_post_async(url, payload)
