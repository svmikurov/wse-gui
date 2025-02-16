"""Exercise models."""

from urllib.parse import urljoin

from toga.sources import Source

from wse.constants import HOST
from wse.constants.url import CALC_ANSWER_PATH, CALC_TASK_PATH, USER_DATA_PATH
from wse.contrib.http_requests import request_get_async, request_post_async
from wse.models.user import User


class TaskModel(Source):
    """Task models with user answer input."""

    _url_user_data = urljoin(HOST, USER_DATA_PATH)
    url_answer: str
    url_task: str
    title: str
    exercise: str

    def __init__(self) -> None:
        """Construct the task."""
        super().__init__()
        self._question: str | None = None
        self._solution: str | None = None
        self._answer: str | None = None

    async def start_new_task(self) -> None:
        """Start a new task."""
        data = await self._request_task(self.url_task)
        self._set_page_data()
        self._set_task_data(data)
        self._display_question()

    def _set_task_data(self, data: dict) -> None:
        self._question = data['question']
        self._solution = data['solution']

    def update_answer(self, answer: str) -> None:
        """Update entered answer."""
        self._answer = answer
        self._display_answer()

    async def check_answer(self) -> None:
        """Check user answer."""
        await self._send_answer(self.url_answer, self._answer)
        await self._update_info_panel()

        if self._solution == self._answer:
            self._clear()
            await self.start_new_task()
        else:
            self._display_result('Неверно!')

    #####################################################################
    # Notifications

    def _clear(self) -> None:
        """Clear values of widgets."""
        self.notify('clear')

    def _display_question(self) -> None:
        self.notify('display_question', text=self._question)

    def _display_answer(self) -> None:
        self.notify('display_answer', text=self._answer)

    def _display_result(self, text: str) -> None:
        self.notify('display_result', text=text)

    def _set_page_data(self) -> None:
        self.notify('set_title', text=self.title)

    async def _update_info_panel(self) -> None:
        response = await request_get_async(self._url_user_data)
        data = response.json()
        text = User.info % data['points']
        self.notify('update_info_panel', text=text)

    #####################################################################
    # HTTP requests

    async def _request_task(self, url: str) -> dict:
        payload = {'exercise': self.exercise}
        response = await request_post_async(url, payload)
        return response.json()

    @staticmethod
    async def _send_answer(url: str, user_answer: str) -> None:
        payload = {'answer': user_answer}
        await request_post_async(url, payload)


class CalculationModel(TaskModel):
    """Calculation model with user input."""

    url_task = urljoin(HOST, CALC_TASK_PATH)
    url_answer = urljoin(HOST, CALC_ANSWER_PATH)


class MultiplicationModel(CalculationModel):
    """Multiplication model with user input."""

    title = 'Таблица умножения'
    exercise = 'mul'
