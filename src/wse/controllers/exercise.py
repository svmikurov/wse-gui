"""Exercise controller."""

from http import HTTPStatus
from pprint import pprint
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
        self._has_assessment = False

        # Sources
        self.question = Source()
        self.answer = Source()
        self.info = Source()
        self.event = Source()

    async def on_open(self, _: toga.Widget) -> None:
        """Start exercise when box was assigned to window content."""
        self._set_exercise_params()
        self._select_widgets_to_display()
        self._reset_task_status()
        await self._loop_exercise()

    def _set_exercise_params(self) -> None:
        """Set lookup conditions of items to use in the exercise."""
        lookup_conditions = self._app.plc_params.lookup_conditions
        self.timer.has_timeout = lookup_conditions.pop('has_timeout')
        self.timer.timeout = lookup_conditions.pop('timeout')
        self._task.params = lookup_conditions

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
                self._change_task_status(next_status='answer')
                self._reset_assessment_event()
            else:
                self._show_answer()
                self._change_task_status(next_status='question')

            if self.timer.has_timeout:
                await self.timer.start()
            else:
                # The exercise cycle round does not start
                # if the exercise is paused.
                self.timer.on_pause()

    ####################################################################
    # Notifications

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
    # Loop exercise nethods

    def _on_loop_exercise(self) -> None:
        """Reset the state to start the loop exercise."""
        self.timer.cancel()
        self.timer.unpause()

    def _is_enable_new_task(self) -> bool:
        """Return `False` to cancel task, `True` otherwise."""
        if not self.timer.is_pause():
            return self._is_visible_page()
        return False

    def _is_visible_page(self) -> bool:
        """Is the box of widget is main window content."""
        return self._app.main_window.content is self._app.box_foreign_exercise

    def _reset_task_status(self) -> None:
        """Reset the task status."""
        self._task.status = None

    def _change_task_status(self, next_status: str) -> None:
        """Change the task status."""
        self._task.status = next_status

    def _reset_assessment_event(self) -> None:
        """Reset event of item assessment."""
        self._has_assessment = False

    ####################################################################
    # HTTP requests

    async def _request_task(self) -> None:
        """Request the task data."""
        response = request_post(self.url_exercise, self._task.params)
        if response.status_code == HTTPStatus.OK:
            self._task.data = response.json()
            pprint(self._task.data)
            return
        # elif response.status_code == HTTPStatus.NO_CONTENT:
        #     # TODO:Add message no task.
        #     await self.move_to_box_params(self)
        self._task.data = None

    async def _update_item_progress(self, assessment: str) -> None:
        """Request to update progress study of item."""
        payload = {'action': assessment, 'item_id': self._task.item_id}
        await request_post_async(self.url_progress, payload)

    ####################################################################
    # Button handlers

    def pause(self, _: toga.Widget) -> None:
        """Pause the task."""
        self.timer.on_pause()

    async def not_know(self, _: toga.Widget) -> None:
        """Mark item in question as not know."""
        if not self._has_assessment:
            await self._update_item_progress(assessment='not_know')
            self._has_assessment = True
        await self._move_to_next_task_status()

    async def know(self, _: toga.Widget) -> None:
        """Mark item in question as know."""
        if not self._has_assessment:
            await self._update_item_progress(assessment='know')
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

    async def _move_to_next_task_status(self) -> None:
        """Move to next task status."""
        await self._loop_exercise()

    ####################################################################
    # Page events

    def _select_widgets_to_display(self) -> None:
        """Select widgets according to exercise parameters."""
        self.event.notify('update_availability_pause_button')
