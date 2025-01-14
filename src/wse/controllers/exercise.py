"""Exercise controller."""

from http import HTTPStatus
from typing import TypeVar

import toga
from toga.sources import Source

from wse.contrib.http_requests import request_post, request_post_async
from wse.contrib.task import Task
from wse.contrib.timer import Timer
from wse.controllers.params import ControllerParams
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
)

T = TypeVar('T')


class ControllerExercise:
    """Exercise controller."""

    def __init__(self, app: T, plc_params: ControllerParams) -> None:
        """Construct the controller."""
        super().__init__()
        self._app = app
        self._plc_params = plc_params
        self.url_exercise = None
        self.url_progress = None
        self.timer = Timer()
        self._task = Task()

        # Sources
        self.question = Source()
        self.answer = Source()
        self.info = Source()
        self.event = Source()

        # Widget conditions
        self.has_progress_bar = False
        self.exercise_page = None

    async def on_open(self, _: toga.Widget) -> None:
        """Start exercise when box was assigned to window content."""
        self._set_exercise_params()
        self._reset_previous_exercise()
        self._select_widgets_to_display()
        await self._loop_exercise()

    def _set_exercise_params(self) -> None:
        """Set lookup conditions of items to use in the exercise."""
        lookup_conditions = self._plc_params.lookup_conditions
        self.timer.has_timeout = lookup_conditions.pop('has_timeout')
        self.timer.timeout = lookup_conditions.pop('timeout')
        self._task.params = lookup_conditions

    ####################################################################
    # Exercise loop

    async def _loop_exercise(self) -> None:
        """Create new task in exercise loop."""
        self._on_loop_exercise()

        while self._is_enable_new_task():
            if self._task.status != 'answer':
                self._reset_previous_events()
                self._request_task()
                if not self._task.data:
                    await self._handle_no_task()
                    break
                self._show_exercise_info()
                self._show_question()
                self._change_task_status(to_status='answer')
            else:
                self._show_answer()
                self._change_task_status(to_status='question')

            if self.timer.has_timeout:
                # Start timeout for each task status.
                await self._start_timeout_progress_bar()
            else:
                # Exercise params not include timeout.
                # The exercise cycle round does not start
                # if the exercise is paused.
                self.timer.on_pause()

    ####################################################################
    # Task notifications

    def _show_question(self) -> None:
        self.question.notify('change', text=self._task.question)
        self.answer.notify('clean')

    def _show_answer(self) -> None:
        self.answer.notify('change', text=self._task.answer)

    def _clean_text_panels(self) -> None:
        for listener in (self.question, self.answer, self.info):
            listener.notify('clean')

    def _show_exercise_info(self) -> None:
        self.info.notify(
            'change',
            text='Прогресс: {}\nКол-во слов: {}'.format(
                self._task.data['assessment'],
                self._task.data['item_count'],
            ),
        )

    #####################################################################
    # Utility methods

    def _reset_previous_exercise(self) -> None:
        # Reset task status.
        self._task.status = None
        # Reset condition has progress bar
        self.has_progress_bar = False

    def _set_progress_bar_availability(self) -> None:
        min_time_for_bar = 3  # sec
        self.has_progress_bar = bool(
            self.timer.has_timeout and self.timer.timeout >= min_time_for_bar
        )

    ####################################################################
    # Exercise loop methods

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
        return self._app.main_window.content is self.exercise_page

    def _reset_previous_events(self) -> None:
        """Reset previous events at page."""
        self._clean_text_panels()
        self._activate_answer_buttons()

    def _change_task_status(self, to_status: str) -> None:
        self._task.status = to_status

    async def _start_timeout_progress_bar(self) -> None:
        await self.timer.start_counter()

    async def _handle_no_task(self) -> None:
        await goto_back_handler(self.exercise_page)

    ####################################################################
    # HTTP requests

    def _request_task(self) -> None:
        """Request the task data."""
        response = request_post(self.url_exercise, self._task.params)
        if response.status_code == HTTPStatus.OK:
            self._task.data = response.json()
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

    def pause(self, widget: toga.Widget) -> None:
        """Pause the task."""
        self.timer.on_pause()
        # Once pressed, the button becomes inactive.
        widget.enabled = False

    async def not_know(self, _: toga.Widget) -> None:
        """Mark item in question as not know."""
        self._deactivate_answer_buttons()
        await self._update_item_progress(assessment='not_know')
        await self._move_to_next_task_status()

    async def know(self, _: toga.Widget) -> None:
        """Mark item in question as know."""
        await self._update_item_progress(assessment='know')
        await self._move_to_next_task()

    async def next(self, _: toga.Widget) -> None:
        """Move to next task status."""
        await self._move_to_next_task_status()

    #########
    # Helpers

    async def _move_to_next_task(self) -> None:
        self._task.status = None
        await self._move_to_next_task_status()

    async def _move_to_next_task_status(self) -> None:
        self._activate_pause_button()
        await self._loop_exercise()

    ####################################################################
    # Page event notifications

    def _select_widgets_to_display(self) -> None:
        """Select widgets according to exercise parameters."""
        self._set_progress_bar_availability()
        self.event.notify('update_availability_pause_button')
        self.event.notify('update_availability_progress_bar')

    def _activate_pause_button(self) -> None:
        self.event.notify('activate_pause_button')

    def _deactivate_answer_buttons(self) -> None:
        # Answer buttons are pressed once per task.
        self.event.notify('deactivate_answer_buttons')

    def _activate_answer_buttons(self) -> None:
        self.event.notify('activate_answer_buttons')
