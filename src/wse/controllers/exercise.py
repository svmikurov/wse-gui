"""Exercise controller."""

from http import HTTPStatus
from typing import TypeVar

import toga
from toga.sources import Source

from wse.contrib.http_requests import request_post
from wse.contrib.task import Task
from wse.contrib.timer import Timer

T = TypeVar('T')


class ControllerExercise:
    """Exercise controller."""

    def __init__(self, app: T) -> None:
        """Construct the controller."""
        super().__init__()
        self.app = app
        self.url_exercise = None
        self.url_progress = None
        self.timer = Timer()
        self.task = Task()

        # Sources
        self.question = Source()
        self.answer = Source()
        self.info = Source()

    async def start(self) -> None:
        """Start the exercise."""
        self._set_task_params()
        await self._loop_task()

    async def _loop_task(self) -> None:
        """Create new task in loop."""
        self.timer.cancel()

        while self._is_enable_new_task():
            if self.task.status != 'answer':
                self._clean_text_panel()
                await self._request_task()
                if not self.task.data:
                    break
                self._show_question()
                self.task.status = 'answer'
            else:
                self._show_answer()
                self.task.status = 'question'

            await self.timer.start()

    def _show_question(self) -> None:
        """Show the question."""
        self.question.notify('change', text=self.task.question)
        self.answer.notify('clean')

    def _show_answer(self) -> None:
        """Show the answer."""
        self.answer.notify('change', text=self.task.answer)

    def _clean_text_panel(self) -> None:
        """Clear the text panel."""
        self.question.notify('clean')
        self.answer.notify('clean')

    ####################################################################
    # Utility methods

    def _is_enable_new_task(self) -> bool:
        """Return `False` to cancel task, `True` otherwise."""
        if not self.timer.is_pause():
            return self._is_visible_page()
        return False

    def _is_visible_page(self) -> bool:
        """Is the box of widget is main_window content."""
        return self.app.main_window.content == self.app.box_foreign_exercise

    def _set_task_params(self) -> None:
        """Set lookup conditions of items to use in the exercise."""
        lookup_conditions = self.app.plc_params.lookup_conditions
        self.task.params = lookup_conditions

    ####################################################################
    # HTTP requests

    async def _request_task(self) -> None:
        """Request the task data."""
        response = request_post(self.url_exercise, self.task.params)
        if response.status_code == HTTPStatus.OK:
            self.task.data = response.json()
            return
        # elif response.status_code == HTTPStatus.NO_CONTENT:
        #     # TODO:Add message no task.
        #     await self.move_to_box_params(self)
        self.task.data = None

    ####################################################################
    # Button handlers

    def pause(self, _: toga.Widget) -> None:
        """Pause the task."""
        pass

    def not_know(self, _: toga.Widget) -> None:
        """Mark item in question as not know."""
        pass

    def know(self, _: toga.Widget) -> None:
        """Mark item in question as know."""
        pass

    def next(self, _: toga.Widget) -> None:
        """Next task."""
        pass
