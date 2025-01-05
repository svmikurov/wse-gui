"""Exercise controller."""
from http import HTTPStatus

import toga
from toga.sources import Source, Listener

from wse.contrib.http_requests import request_post
from wse.contrib.task import Task
from wse.contrib.timer import Timer


class ListenerData:
    """The data for listener of controller."""

    __slots__ = ('name', 'accessor', 'value')

    def __init__(self, name: str, accessor: str, value: object) -> None:
        """Construct the data."""
        self.name = name
        self.accessor = accessor
        self.value = value


class ControllerExercise(Source):
    """Exercise controller."""

    def __init__(self) -> None:
        """Construct a exercise."""
        super().__init__()
        self.timer = Timer()
        self.task = Task()
        self.is_exercise = False

        self.url_exercise = ''

        # Listeners data
        self.question = ListenerData('text_panel_question', 'value', '')
        self.answer = ListenerData('text_panel_answer', 'value', '')
        self.info = ListenerData('text_panel_info', 'value', '')

    async def loop_task(self) -> None:
        """Show new task in loop."""
        self.timer.cancel()

        while self.is_enable_new_task():
            if self.task.status != 'answer':
                self.clean_text_panel()
                await self.request_task()
                if not self.task.data:
                    break
                self.show_question()
                self.task.status = 'answer'
            else:
                self.show_answer()
                self.task.status = 'question'
            await self.timer.start()

    def is_enable_new_task(self):
        pass


    def clean_text_panel(self) -> None:
        self.notify('clear', listener=self.question)
        self.notify('clear', listener=self.answer)

    async def request_task(self) -> None:
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

    def pause(self, _: toga.Widget):
        pass

    def not_know(self, _: toga.Widget):
        pass

    def know(self, _: toga.Widget):
        pass

    def next(self, _: toga.Widget):
        pass

