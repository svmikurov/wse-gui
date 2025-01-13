"""Exercise."""

import toga
from toga.constants import COLUMN
from toga.style.pack import Pack

from wse.controllers.exercise import ControllerExercise
from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import AnswerBtn, BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.progress_bar import ProgressBarApp
from wse.pages.widgets.text_input import MultilineTextInputApp, TextPanel


class ExerciseWidgets:
    """Exercise widgets."""

    title = ''

    def __init__(self, controller: ControllerExercise) -> None:
        """Construct a exercise widgets."""
        super().__init__()
        self.plc = controller

        # fmt: off
        # Style
        label_style = Pack(padding=(0, 0, 0, 7))

        # Title
        self.label_title = TitleLabel(self.title)

        # Labels
        self.label_question = toga.Label('Вопрос:', style=label_style)
        self.label_answer = toga.Label('Ответ:', style=label_style)

        # Progress bar
        self.progress_bar = ProgressBarApp(max=self.plc.timer.timeout)

        # Task text display widgets
        self.text_panel_question = TextPanel(style=Pack(flex=2))
        self.text_panel_answer = TextPanel(style=Pack(flex=2))

        # Task info display widgets
        self.label_text_panel = toga.Label('Информация об упражнении:')
        self.label_text_panel.style = Pack(padding=(0, 0, 0, 7))
        self.text_panel_info = MultilineTextInputApp(style=Pack(flex=1), readonly=True)  # noqa: E501

        # Exercise buttons
        self.btn_pause = AnswerBtn('Пауза', on_press=self.plc.pause)
        self.btn_not_know = AnswerBtn('Не знаю', on_press=self.plc.not_know)
        self.btn_know = AnswerBtn('Знаю', on_press=self.plc.know)
        self.btn_next = AnswerBtn('Далее', on_press=self.plc.next)

        # Navigation buttons
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # Listeners
        self.plc.question.add_listener(self.text_panel_question)
        self.plc.answer.add_listener(self.text_panel_answer)
        self.plc.info.add_listener(self.text_panel_info)
        self.plc.timer.progress_bar_source.add_listener(self.progress_bar)
        # fmt: on

    async def on_open(self, widget: toga.Widget) -> None:
        """Start exercise when box was assigned to window content."""
        await self.plc.on_open(widget)


class ExerciseLayout(ExerciseWidgets, BaseBox):
    """Layout of exercise box-container."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)

        # Some widgets are enclosed in box.
        self.box_btns = toga.Box(style=Pack(height=100))
        self.box_progress_bar = toga.Box(style=Pack(direction=COLUMN))

        # DOM.
        self.add(
            self.box_progress_bar,
            self.label_question,
            self.text_panel_question,
            self.label_answer,
            self.text_panel_answer,
            self.label_text_panel,
            self.text_panel_info,
            self.box_btns,
            self.btn_goto_back,
        )
        self.box_btns.add(
            self.btn_pause,
            self.btn_not_know,
            self.btn_know,
            self.btn_next,
        )
        self.box_progress_bar.add(
            self.progress_bar,
        )

    ####################################################################
    # Notifications

    def update_availability_pause_button(self) -> None:
        """Update the availability of the pause button."""
        if self.plc.timer.has_timeout:
            self.box_btns.insert(0, self.btn_pause)
        else:
            self.box_btns.remove(self.btn_pause)

    def activate_pause_button(self) -> None:
        """Activate the pause button."""
        # Pause button deactivated on press with button handler.
        self.btn_pause.enabled = True

    def deactivate_answer_buttons(self) -> None:
        """Deactivate answer button."""
        # Answer buttons are pressed once per task.
        for button in (self.btn_know, self.btn_not_know):
            button.enabled = False

    def activate_answer_buttons(self) -> None:
        """Activate answer button."""
        for button in (self.btn_know, self.btn_not_know):
            button.enabled = True

    def update_availability_progress_bar(self) -> None:
        """Update the availability of the progress bar."""
        if self.plc.has_progress_bar:
            self.insert(0, self.box_progress_bar)
        else:
            self.remove(self.box_progress_bar)
