"""Exercise controller."""

from http import HTTPStatus
from typing import TypeVar

import toga
from toga.sources import Source

from wse.contrib.http_requests import request_post, request_post_async
from wse.contrib.task import Task
from wse.contrib.timer import Timer

T = TypeVar('T')


class ControllerExercise:
    """Exercise controller."""

    def __init__(self, app: T) -> None:
        """Construct the controller."""
        super().__init__()
        self._app = app
        self.url_exercise = None
        self.url_progress = None
        self.timer = Timer()
        self._task = Task()
        self._has_action = False

        # Sources
        self.question = Source()
        self.answer = Source()
        self.info = Source()
        self.event = Source()

    async def on_open(self, _: toga.Widget) -> None:
        """Start exercise when box was assigned to window content."""
        self._set_exercise_params()
        self._select_widgets()
        self._reset_task_status()
        await self._loop_exercise()

    ####################################################################
    # Loop exercise

    async def _loop_exercise(self) -> None:
        """Create new task in exercise loop."""
        self._on_loop_exercise()

        while self._is_enable_new_task():
            if self._task.status != 'answer':
                self._clean_text_panel()
                await self._request_task()
                if not self._task.data:
                    break
                self._show_question()
                self._task.status = 'answer'
                self._has_action = False
            else:
                self._show_answer()
                self._task.status = 'question'

            if self.timer.has_timeout:
                await self.timer.start()
            else:
                # The exercise cycle round does not start
                # if the exercise is paused.
                self.timer.on_pause()

    def _on_loop_exercise(self):
        """Reset the state to start the loop exercise."""
        self.timer.cancel()
        self.timer.unpause()

    def _show_question(self) -> None:
        """Show the question."""
        self.question.notify('change', text=self._task.question)
        self.answer.notify('clean')

    def _show_answer(self) -> None:
        """Show the answer."""
        self.answer.notify('change', text=self._task.answer)

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
        """Is the box of widget is main window content."""
        return self._app.main_window.content is self._app.box_foreign_exercise

    def _set_exercise_params(self) -> None:
        """Set lookup conditions of items to use in the exercise."""
        lookup_conditions = self._app.plc_params.lookup_conditions
        self.timer.has_timeout = lookup_conditions.pop('has_timeout')
        self.timer.timeout = lookup_conditions.pop('timeout')
        self._task.params = lookup_conditions

    def _reset_task_status(self):
        """Reset the task status."""
        self._task.status = None

    ####################################################################
    # HTTP requests

    async def _request_task(self) -> None:
        """Request the task data."""
        response = request_post(self.url_exercise, self._task.params)
        if response.status_code == HTTPStatus.OK:
            self._task.data = response.json()
            return
        # elif response.status_code == HTTPStatus.NO_CONTENT:
        #     # TODO:Add message no task.
        #     await self.move_to_box_params(self)
        self._task.data = None

    async def _update_item_progress(self, action):
        """Request to update progress study of item."""
        payload = {'action': action, 'item_id': self._task.item_id}
        await request_post_async(self.url_progress, payload)

    ####################################################################
    # Button handlers

    def pause(self, _: toga.Widget) -> None:
        """Pause the task."""
        self.timer.on_pause()

    async def not_know(self, _: toga.Widget) -> None:
        """Mark item in question as not know."""
        if not self._has_action:
            await self._update_item_progress(action='not_know')
            self._has_action = True
        await self._move_to_next_task_status()

    async def know(self, _: toga.Widget) -> None:
        """Mark item in question as know."""
        if not self._has_action:
            await self._update_item_progress(action='know')
        await self._move_to_next_task()

    async def next(self, _: toga.Widget) -> None:
        """Move to next task status."""
        await self._move_to_next_task_status()

    #########
    # Helpers

    async def _move_to_next_task(self) -> None:
        """Move to next task."""
        self._task.status = None
        await self._move_to_next_task_status()

    async def _move_to_next_task_status(self):
        """Move to next task status."""
        await self._loop_exercise()

    ####################################################################
    # Page events

    def _select_widgets(self) -> None:
        """Select widgets according to exercise parameters."""
        self.event.notify('update_availability_pause_button')
