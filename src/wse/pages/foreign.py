"""Foreign pages."""

from urllib.parse import urljoin

import toga
from toga.style import Pack

from wse import constants as const
from wse.constants import TEXT_DISPLAY_FONT_SIZE
from wse.controllers.form import WordFormController
from wse.pages.containers.exercise import ExerciseLayout
from wse.pages.containers.form import FormLayout
from wse.pages.containers.params import ParamsLayout
from wse.pages.containers.table import TableLayout
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_foreign_create_handler,
    goto_foreign_exercise_handler,
    goto_foreign_params_handler,
    goto_foreign_table_handler,
    goto_foreign_tasks_handler,
    goto_foreign_test_handler,
    goto_foreign_update_handler,
)
from wse.pages.widgets.box_page import BaseBox, WidgetMixin
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import InfoTextPanel, InputTextField

ACCESSORS = ['id', 'foreign_word', 'native_word']


class MainForeignPage(WidgetMixin, BaseBox):
    """Foreign main pages."""

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()

        self.label_title = TitleLabel(const.TITLE_FOREIGN_MAIN)

        # Buttons
        self.btn_goto_tasks = BtnApp(
            const.BTN_GOTO_FOREIGN_TASKS, on_press=goto_foreign_tasks_handler
        )
        self.btn_goto_params = BtnApp(
            const.BTN_GOTO_FOREIGN_PARAMS,
            on_press=goto_foreign_params_handler,
        )
        self.btn_goto_create = BtnApp(
            const.BTN_GOTO_FOREIGN_CREATE,
            on_press=goto_foreign_create_handler,
        )
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # The buttons are located at the bottom of the pages.
        self.box_alignment = toga.Box(style=Pack(flex=1))

        # DOM
        self.add(
            self.label_title,
            self.box_alignment,
            self.btn_goto_create,
            self.btn_goto_tasks,
            self.btn_goto_params,
            self.btn_goto_back,
        )


class ParamsForeignPage(ParamsLayout):
    """Foreign exercise params pages."""

    title = const.TITLE_FOREIGN_PARAMS
    url = urljoin(const.HOST, const.FOREIGN_PARAMS_PATH)
    goto_exercise_handler = goto_foreign_exercise_handler
    goto_table_handler = goto_foreign_table_handler


class ExerciseForeignPage(ExerciseLayout):
    """Foreign exercise pages."""

    title = const.TITLE_FOREIGN_EXERCISE
    url_exercise = urljoin(const.HOST, const.FOREIGN_EXERCISE_PATH)
    url_progress = urljoin(const.HOST, const.FOREIGN_ASSESSMENT_PATH)
    url_favorites = urljoin(const.HOST, const.FOREIGN_FAVORITES_PATH)


class WordForm(FormLayout):
    """Word form container."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the form."""
        super().__init__(*args, **kwargs)

        # Word data input widgets
        self._input_native = InputTextField(
            style=Pack(
                flex=1,
                font_size=TEXT_DISPLAY_FONT_SIZE,
                padding_bottom=1,
            ),
            placeholder='Слово на родном языке',
            on_change=self._plc.native_word.change,
        )
        self._input_foreign = InputTextField(
            style=Pack(
                flex=1,
                font_size=TEXT_DISPLAY_FONT_SIZE,
            ),
            placeholder='Слово на иностранном языке',
            on_change=self._plc.foreign_word.change,
        )

        # Update DOM
        self.insert(1, self._input_foreign)
        self.insert(2, self._input_native)

    #####################################################################
    # Notification methods

    def populate_form(self, data: WordFormController) -> None:
        """Set initial values for form input widgets."""
        self._input_native.value = data.native_word.value
        self._input_foreign.value = data.foreign_word.value

    def clear_form(self) -> None:
        """Clear the form."""
        self._input_native.value = ''
        self._input_foreign.value = ''

    #####################################################################
    # Interactive methods

    def _focus_to_input_field(self) -> None:
        self._input_foreign.focus()


class CreateWordPage(WordForm):
    """Word create pages."""

    title = const.TITLE_FOREIGN_CREATE
    url = urljoin(const.HOST, const.FOREIGN_PATH)
    submit_text = 'Добавить'
    accessors = ACCESSORS


class UpdateWordPage(WordForm):
    """Word update pages."""

    title = const.TITLE_FOREIGN_UPDATE
    url = urljoin(const.HOST, const.FOREIGN_DETAIL_PATH)
    submit_text = 'Изменить'
    accessors = ACCESSORS


class TableWordPage(TableLayout):
    """Wordlist table pages."""

    title = const.TITLE_FOREIGN_LIST
    url = urljoin(const.HOST, const.FOREIGN_SELECTED_PATH)
    url_detail = urljoin(const.HOST, const.FOREIGN_DETAIL_PATH)
    table_headings = ['На иностранном', 'На родном']
    table_accessors = ['foreign_word', 'native_word']
    source_accessors = ACCESSORS

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the pages."""
        super().__init__(*args, **kwargs)
        self._plc.goto_create_handler = goto_foreign_create_handler
        self._plc.goto_update_handler = goto_foreign_update_handler


class TasksForeignPage(BaseBox):
    """Foreign tasks pages."""

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()
        self._label_title = TitleLabel(const.TITLE_FOREIGN_TASKS)

        # Info panel
        self._info_panel = InfoTextPanel(style=Pack(flex=1), value='')

        # fmt: off
        # Navigation buttons
        self._btn_goto_test = BtnApp('Тест', on_press=goto_foreign_test_handler)  # noqa: E501
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

        # DOM
        self.add(
            self._label_title,
            self._info_panel,
            self._btn_goto_test,
            self._btn_goto_back,
        )
