"""Exercise models."""
import asyncio
from urllib.parse import urljoin

from toga.sources import Source

from wse.constants import HOST
from wse.constants.url import CALC_TASK_PATH, CALC_ANSWER_PATH
from wse.contrib.http_requests import request_get_async, request_post_async


class _TaskModel(Source):
    """Task models with user answer input."""

    url_task: str
    url_answer: str
    title: str

    def __init__(self) -> None:
        """Construct the task."""
        super().__init__()
        self._question: str | None = None
        self._answer: str | None = None
        self._user_answer: str | None = None

    async def start_new_task(self) -> None:
        """Start a new task."""
        data = await self._request_task(self.url_task)
        self._set_page_data()
        self._save_task_data(data)
        self._display_question()

    def _save_task_data(self, data: dict) -> None:
        self._question = data['question']
        self._answer = data['answer']

    def update_user_answer(self, user_answer: str) -> None:
        """Update entered answer."""
        self._user_answer = user_answer
        self._display_user_answer()

    async def check_user_answer(self) -> None:
        """Clear entered answer."""
        await self._send_answer(self.url_answer, self._user_answer)

        if self._user_answer == self._answer:
            self._clear()
            await self.start_new_task()
        else:
            self._display_result('Неверно!')

    #####################################################################
    # Notifications

    def _clear(self) -> None:
        """Clear previous values of widgets."""
        self.notify('clear')

    def _display_question(self) -> None:
        self.notify('display_question', text=self._question)

    def _display_user_answer(self) -> None:
        self.notify('display_user_answer', text=self._user_answer)

    def _display_result(self, text: str) -> None:
        self.notify('display_result', text=text)

    def _set_page_data(self) -> None:
        self.notify('set_title', text=self.title)

    #####################################################################
    # HTTP requests

    @staticmethod
    async def _request_task(url: str) -> dict:
        response = await request_get_async(url)
        return response.json()

    @staticmethod
    async def _send_answer(url: str, user_answer: str) -> None:
        payload = {'answer': user_answer}
        await request_post_async(url, payload)


class CalcModel(_TaskModel):
    """Calculations model with user input."""

    url_task = urljoin(HOST, CALC_TASK_PATH)
    url_answer = urljoin(HOST, CALC_ANSWER_PATH)
    title = 'Упражнение на вычисления'

    @staticmethod
    async def _request_task(url: str) -> dict:
        payload = {'exercise_type': 'mul'}
        response = await request_post_async(url, payload)
        return response.json()
