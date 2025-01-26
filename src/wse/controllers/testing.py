"""Test exercise controller."""

import json
from typing import TypeVar

import toga
from toga.sources import Source

from wse.contrib.http_requests import request_get_async, request_post_async

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
        self.choices: list[list[str, str]] = data['choices']


class ChoiceSource(Source):
    """The choice widget source."""

    def __init__(self, value: object = None, accessor: str = 'value') -> None:
        """Construct the source."""
        super().__init__()
        self.accessor = accessor
        setattr(self, accessor, value)

    def set_value(self, value: str | int | None = None) -> None:
        """Set the initial value for the widget."""
        self.notify('set_value', value=value)

    def update_value(self, widget: toga.Widget) -> None:
        """Update the source value."""
        value = getattr(widget, self.accessor)
        setattr(self, self.accessor, value)


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
        """Invoke methods on page open."""
        await self._display_task()

    #####################################################################
    # Source methods

    def create_source(self, index: str) -> SourceT:
        """Create choice text source."""
        setattr(self, self._choice_source_name % index, ChoiceSource())
        return self._get_source(index)

    def _get_source(self, index: str) -> SourceT:
        return getattr(self, self._choice_source_name % index)

    #####################################################################
    # Task methods

    async def _create_task(self) -> None:
        task_data = await self._request_task(self.url_question)
        self.task = Task(task_data)

    async def _display_task(self) -> None:
        """Display the test exercise task."""
        await self._create_task()
        self._remove_choices()
        self._create_choices(self.task.choices)
        self._add_choices(self.task.choices)
        self._populate_question(self.task.question)
        self._populate_choices(self.task.choices)

    @property
    def answers(self) -> list[str]:
        """User answer choices."""
        answers = []
        for index, _ in self.task.choices:
            source = self._get_source(index)
            if source.value:
                answers.append(index)
        return answers

    #####################################################################
    # Button handlers

    def submit_handler(self, _: toga.Widget) -> None:
        """Submit the answer, button handler."""

    def next_handler(self, _: toga.Widget) -> None:
        """Start the next test task, button handler."""
        pass

    #####################################################################
    # Notify listeners

    def _create_choices(self, choices: list[list[str, str]]) -> None:
        self.notify('create_choices', choices=choices)

    def _add_choices(self, choices: list[list[str, str]]) -> None:
        self.notify('add_choices', choices=choices)

    def _populate_choices(self, choices: list[list[str, str]]) -> None:
        self.notify('populate_choices', choices=choices)

    def _remove_choices(self) -> None:
        self.notify('remove_choices')

    def _populate_question(self, question: str) -> None:
        self.notify('populate_question', question=question)

    #####################################################################
    # Http requests

    @staticmethod
    async def _request_task(url: str) -> dict:
        r = await request_get_async(url)
        data = r.json()
        return json.loads(data)

    @staticmethod
    async def _send_answer(url: str, payload: dict) -> None:
        await request_post_async(url, payload)
