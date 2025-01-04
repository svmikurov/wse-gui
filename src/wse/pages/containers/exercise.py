"""Exercise."""

from http import HTTPStatus

import toga
from toga.style.pack import COLUMN, ROW, Pack

from wse.constants import (
    NO_TASK_MSG,
    TASK_ERROR_MSG,
)
from wse.contrib.http_requests import (
    request_post,
    request_post_async,
)
from wse.contrib.task import Task
from wse.contrib.timer import Timer
from wse.pages.containers.params import ParamsWidgets
from wse.pages.widgets.box_page import BaseBox, WidgetMixin
from wse.pages.widgets.button import AnswerBtn
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import TextPanel


class Exercise:
    """Exercise."""

    url_exercise = ''
    """The exercise url (`str`).
    """
    url_progress = ''
    """The url to update a item study progress (`str`).
    """

    def __init__(self) -> None:
        """Construct a exercise."""
        super().__init__()
        self.timer = Timer()
        self.task = Task()

    async def on_open(self, widget: toga.Widget) -> None:
        """Start exercise when box was assigned to window content."""
        self.set_params()
        self.reset_task_status()
        await self.loop_task()

    async def move_to_next_task(self) -> None:
        """Move to next task."""
        self.task.status = 'question'
        await self.loop_task()

    def set_params(self) -> None:
        """Set exercise params to exercise attr."""
        box_params = self.get_box_params()
        self.task.params = box_params.get_params()

    async def request_task(self) -> None:
        """Request the task data."""
        response = request_post(self.url_exercise, self.task.params)
        if response.status_code == HTTPStatus.OK:
            self.task.data = response.json()
            return
        elif response.status_code == HTTPStatus.NO_CONTENT:
            await self.show_message('', NO_TASK_MSG)
            await self.move_to_box_params(self)
        else:
            await self.show_message('', TASK_ERROR_MSG)
        self.task.data = None

    def show_question(self) -> None:
        """Show the task question without an answer."""
        self.text_panel_question.update(self.task.question)
        self.text_panel_answer.clean()

    def show_answer(self) -> None:
        """Show the task answer."""
        self.text_panel_answer.update(self.task.answer)

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

    def reset_task_status(self) -> None:
        """Reset the task status."""
        self.task.status = None

    def is_enable_new_task(self) -> bool:
        """Return `False` to cancel task update, `True` otherwise."""
        if not self.timer.is_pause():
            return self.is_visible_box()
        return False

    ####################################################################
    # Utility methods for exercise

    def get_box_params(self) -> ParamsWidgets:
        """Get box instance of exercise params."""
        raise NotImplementedError(
            'Subclasses must provide a box_name_params method.'
        )


class ExerciseWidgets(Exercise):
    """Exercise widgets."""

    title = ''
    """The page title (`str`).
    """

    def __init__(self) -> None:
        """Construct a exercise widgets."""
        super().__init__()

        # Style.
        label_style = Pack(padding=(0, 0, 0, 7))

        # Title.
        self.label_title = TitleLabel(self.title)

        # Labels.
        self.label_question = toga.Label('Вопрос:', style=label_style)
        self.label_answer = toga.Label('Ответ:', style=label_style)

        # Text display widgets.
        self.text_panel_question = TextPanel(style=Pack(flex=2))
        self.text_panel_answer = TextPanel(style=Pack(flex=2))

        # Exercise buttons.
        self.btn_pause = AnswerBtn('Пауза', self.pause_handler)
        self.btn_not_know = AnswerBtn('Не знаю', self.not_know_handler)
        self.btn_know = AnswerBtn('Знаю', self.know_handler)
        self.btn_next = AnswerBtn('Далее', self.next_handler)

    async def on_open(self, widget: toga.Widget) -> None:
        """Start exercise when box was assigned to window content."""
        await super().on_open(widget)
        self.clean_text_panel()

    async def know_handler(self, _: toga.Widget) -> None:
        """Mark that know the answer, button handler."""
        know_payload = {'action': 'know', 'item_id': self.task.item_id}
        await request_post_async(self.url_progress, know_payload)
        await self.move_to_next_task()

    async def not_know_handler(self, _: toga.Widget) -> None:
        """Mark that not know the answer, button handler."""
        not_know_payload = {'action': 'not_know', 'item_id': self.task.item_id}
        await request_post_async(self.url_progress, not_know_payload)
        await self.move_to_next_task()

    async def move_to_box_params(self, widget: toga.Widget) -> None:
        """Move to exercise parameters page box."""
        raise NotImplementedError(
            'Subclasses must provide a move_to_box_params method.'
        )

    def clean_text_panel(self) -> None:
        """Clean the test panel."""
        self.text_panel_answer.clean()
        self.text_panel_question.clean()

    ####################################################################
    # Task control.

    def pause_handler(self, _: toga.Widget) -> None:
        """Exercise pause, button handler."""
        self.timer.on_pause()

    async def next_handler(self, _: toga.Widget) -> None:
        """Switch to the next task, button handler."""
        self.timer.unpause()
        await self.loop_task()


class ExerciseLayout(WidgetMixin, ExerciseWidgets, BaseBox):
    """Layout of exercise box-container."""

    def __init__(self) -> None:
        """Construct the box."""
        super().__init__()

        # The exercise widgets are enclosed in ``box_exercise``.
        self.box_exercise = toga.Box(style=Pack(direction=COLUMN, flex=1))

        # The exercise buttons are enclosed in ``box_btn_group``.
        self.box_btn_group = toga.Box(style=Pack(direction=ROW, height=100))

        # DOM.
        self.box_exercise.add(
            self.label_question,
            self.text_panel_question,
            self.label_answer,
            self.text_panel_answer,
            self.box_btn_group,
        )
        self.box_btn_group.add(
            self.btn_pause,
            self.btn_not_know,
            self.btn_know,
            self.btn_next,
        )

    def is_visible_box(self) -> bool:
        """Is the box of widget is main_window content."""
        return self.root.app.main_window.content == self
