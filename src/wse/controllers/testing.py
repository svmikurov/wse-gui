"""Test exercise controller."""

from typing import TypeVar

import toga
from toga.sources import Source

from wse.contrib.http_requests import request_post_async

SourceT = TypeVar('SourceT', bound=Source)

TASK = {
    'question': 'question',
    'answer': '3',
    'choices': (
        ('1', 'answer var 1'),
        ('2', 'answer answer answer answer answer answer var 2'),
        ('3', 'answer var 3'),
        ('4', 'answer var 4'),
        ('5', 'answer var 5'),
        ('6', 'answer var 6'),
        ('7', 'answer var 7'),
    ),
}


class Task:
    """Task wrapper."""

    def __init__(self, data: dict) -> None:
        """Construct the task."""
        self.question: str = data['question']
        self.answer: str = data['answer']
        self.choices: tuple[tuple[str, str], ...] = data['choices']


class ControllerTest(Source):
    """Test exercise controller."""

    url_question: str
    url_answer: str
    _choice_source_name = '_choice_source_%s'

    def __init__(self) -> None:
        """Construct the controller."""
        super().__init__()
        self.task: Task | None = None

    async def on_open(self, _: toga.Widget) -> None:
        """Request task."""
        task_data = await self._request_task(self.url_question)
        self.task = Task(task_data)
        self._create_choices(self.task.choices)
        self._add_choices(self.task.choices)
        self._populate_question(self.task.question)
        self._populate_choices(self.task.choices)

    #####################################################################
    # Sources

    def create_source(self, index) -> SourceT:
        """Create choice text source."""
        setattr(self, self._choice_source_name % index, '')
        return getattr(self, self._choice_source_name % index)

    #####################################################################
    # Notify listeners

    def _create_choices(
        self, choices: tuple[tuple[str, str], ...]
    ) -> None:
        self.notify('create_choices', choices=choices)

    def _add_choices(self, choices: tuple[tuple[str, str], ...]) -> None:
        self.notify('add_choices', choices=choices)

    def _populate_question(self, question: str) -> None:
        self.notify('populate_question', question=question)

    def _populate_choices(
        self, choices: tuple[tuple[str, str], ...]
    ) -> None:
        self.notify('populate_choices', choices=choices)

    #####################################################################
    # Http requests

    @staticmethod
    async def _request_task(url: str) -> dict:
        # r = await request_get_async(url)
        # return r.json()
        return TASK

    @staticmethod
    async def _send_answer(url: str, payload: dict) -> None:
        await request_post_async(url, payload)
