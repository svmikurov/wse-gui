"""Exercise."""

import toga
from toga.constants import COLUMN
from toga.style.pack import Pack

from wse.page.handlers.goto_handler import goto_back_handler
from wse.page.widgets.box_page import BaseBox
from wse.page.widgets.button import AnswerBtn, BtnApp
from wse.page.widgets.label import TitleLabel
from wse.page.widgets.progress_bar import ProgressBarApp
from wse.page.widgets.text_input import ExerciseTextPanel, InfoTextPanel


class ExerciseWidgets:
    """Exercise widgets."""

    title = ''
    url_exercise: str
    url_progress: str
    url_favorites: str

    def __init__(self, controller: object) -> None:
        """Construct a exercise widgets."""
        super().__init__()
        self._plc = controller
        self._plc.exercise_page = self
        self._plc.url_exercise = self.url_exercise
        self._plc.url_progress = self.url_progress
        self._plc.url_favorites = self.url_favorites

        # fmt: off
        # Style
        _label_style = Pack(padding=(0, 0, 0, 7))

        # Title
        self._label_title = TitleLabel(self.title)

        # Labels
        self._label_question = toga.Label('Вопрос:', style=_label_style)
        self._label_answer = toga.Label('Ответ:', style=_label_style)

        # Progress bar
        self._progress_bar = ProgressBarApp(max=self._plc.timer.timeout)

        # Task text display widgets
        self._text_panel_question = ExerciseTextPanel(style=Pack(flex=2))
        self._text_panel_answer = ExerciseTextPanel(style=Pack(flex=2))

        # Task info display widgets
        self._label_text_panel = toga.Label('Информация об упражнении:')
        self._label_text_panel.style = Pack(padding=(0, 0, 0, 7))
        self._text_panel_info = InfoTextPanel()

        # Exercise buttons
        self._btn_pause = AnswerBtn('Пауза', on_press=self._plc.pause)
        self._btn_not_know = AnswerBtn('Не знаю', on_press=self._plc.not_know)
        self._btn_know = AnswerBtn('Знаю', on_press=self._plc.know)
        self._btn_next = AnswerBtn('Далее', on_press=self._plc.next)
        self._btn_favorites = BtnApp('Избранное', on_press=self._plc.favorites)

        # Navigation buttons
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # Listeners
        self._plc.question.add_listener(self._text_panel_question)
        self._plc.answer.add_listener(self._text_panel_answer)
        self._plc.info.add_listener(self._text_panel_info)
        self._plc.timer.progress_bar_source.add_listener(self._progress_bar)
        # fmt: on

    async def on_open(self, widget: toga.Widget) -> None:
        """Start exercise when box was assigned to window content."""
        await self._plc.on_open(widget)


class ExerciseLayout(ExerciseWidgets, BaseBox):
    """Layout of exercise box-container."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the box."""
        super().__init__(*args, **kwargs)

        # Some widgets are enclosed in box.
        self._box_btns = toga.Box(style=Pack(height=100))
        self._box_progress_bar = toga.Box(style=Pack(direction=COLUMN))

        # DOM.
        self.add(
            self._box_progress_bar,
            self._label_question,
            self._text_panel_question,
            self._label_answer,
            self._text_panel_answer,
            self._label_text_panel,
            self._text_panel_info,
            self._box_btns,
            self._btn_favorites,
            self._btn_goto_back,
        )
        self._box_btns.add(
            self._btn_pause,
            self._btn_not_know,
            self._btn_know,
            self._btn_next,
        )
        self._box_progress_bar.add(
            self._progress_bar,
        )

    ####################################################################
    # Layout notifications

    def update_availability_pause_button(self) -> None:
        """Update the availability of the pause button."""
        if self._plc.timer.has_timeout:
            self._box_btns.insert(0, self._btn_pause)
        else:
            self._box_btns.remove(self._btn_pause)

    def activate_pause_button(self) -> None:
        """Activate the pause button."""
        self._btn_pause.activate()

    def deactivate_answer_buttons(self) -> None:
        """Deactivate answer button."""
        # Answer buttons are pressed once per task.
        for button in (self._btn_know, self._btn_not_know):
            button.deactivate()

    def activate_answer_buttons(self) -> None:
        """Activate answer button."""
        for button in (self._btn_know, self._btn_not_know):
            button.activate()

    def update_availability_progress_bar(self) -> None:
        """Update the availability of the progress bar."""
        if self._plc.has_progress_bar:
            self.insert(0, self._box_progress_bar)
        else:
            self.remove(self._box_progress_bar)

    def update_favorites_button(self, is_favorites: bool) -> None:
        """Update the favorites button."""
        if is_favorites:
            self._btn_favorites.text = 'Убрать из избранного'
        else:
            self._btn_favorites.text = 'Добавить в избранное'
