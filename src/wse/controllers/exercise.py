"""Exercise controller."""

from http import HTTPStatus

import toga

from wse.contrib.http_requests import request_post
from wse.contrib.task import Task
from wse.contrib.timer import Timer
from wse.sources.exercise import SourceExercise


# TODO: Add style to class for annotation.
class ControllerExercise:
    """Exercise controller."""

    def __init__(self, app: object) -> None:
        """Construct a exercise."""
        super().__init__()
        self.app = app
        self.url_exercise = None
        self.url_progress = None
        self.timer = Timer()
        self.task = Task()

        # Sources
        self.question = SourceExercise()
        self.answer = SourceExercise()
        self.info = SourceExercise()

    async def start(self) -> None:
        """Start the exercise."""
        lookup_conditions = self.get_lookup_conditions()
        self.task.params = lookup_conditions
        await self.loop_task()

    def get_lookup_conditions(self) -> dict:
        """Get the lookup conditions."""
        return self.app.plc_params.lookup_conditions

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

    def is_enable_new_task(self) -> bool:
        """Return `False` to cancel task update, `True` otherwise."""
        if not self.timer.is_pause():
            return self.is_visible_page()
        return False

    def is_visible_page(self) -> bool:
        """Is the box of widget is main_window content."""
        return self.app.main_window.content == self.app.box_foreign_exercise

    def show_question(self) -> None:
        """Show the question."""
        self.question.notify('change', text=self.task.question)
        self.answer.notify('clean')

    def show_answer(self) -> None:
        """Show the answer."""
        self.answer.notify('change', text=self.task.answer)

    def clean_text_panel(self) -> None:
        """Clear the text panel."""
        self.question.notify('clean')
        self.answer.notify('clean')

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
