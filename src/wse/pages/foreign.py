"""Foreign words page boxes."""

from urllib.parse import urljoin

import toga
from toga.style import Pack

from wse.constants import (
    BTN_GOTO_FOREIGN_CREATE,
    BTN_GOTO_FOREIGN_PARAMS,
    FOREIGN_ASSESSMENT_PATH,
    FOREIGN_DETAIL_PATH,
    FOREIGN_EXERCISE_PATH,
    FOREIGN_FAVORITES_PATH,
    FOREIGN_PARAMS_PATH,
    FOREIGN_PATH,
    FOREIGN_SELECTED_PATH,
    HOST,
    TITLE_FOREIGN_CREATE,
    TITLE_FOREIGN_EXERCISE,
    TITLE_FOREIGN_LIST,
    TITLE_FOREIGN_MAIN,
    TITLE_FOREIGN_PARAMS,
    TITLE_FOREIGN_UPDATE,
)
from wse.pages.containers.exercise import (
    ExerciseLayout,
)
from wse.pages.containers.form import ForeignFormLayout
from wse.pages.containers.params import ParamsLayout
from wse.pages.containers.table import TableLayout
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_foreign_create_handler,
    goto_foreign_exercise_handler,
    goto_foreign_params_handler,
    goto_foreign_table_handler,
    goto_foreign_update_handler,
)
from wse.pages.widgets.box_page import BaseBox, WidgetMixin
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel

ACCESSORS = ['id', 'foreign_word', 'native_word']


class MainForeignPage(WidgetMixin, BaseBox):
    """Learning foreign words the main page box."""

    def __init__(self) -> None:
        """Construct the box."""
        super().__init__()

        self.label_title = TitleLabel(TITLE_FOREIGN_MAIN)

        # Buttons
        self.btn_goto_params = BtnApp(
            BTN_GOTO_FOREIGN_PARAMS,
            on_press=goto_foreign_params_handler,
        )
        self.btn_goto_create = BtnApp(
            BTN_GOTO_FOREIGN_CREATE,
            on_press=goto_foreign_create_handler,
        )
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # The buttons are located at the bottom of the page.
        self.box_alignment = toga.Box(style=Pack(flex=1))

        # DOM
        self.add(
            self.label_title,
            self.box_alignment,
            self.btn_goto_create,
            self.btn_goto_params,
            self.btn_goto_back,
        )


class ParamsForeignPage(ParamsLayout):
    """Learning foreign words exercise parameters the page box."""

    title = TITLE_FOREIGN_PARAMS

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self.plc.url = urljoin(HOST, FOREIGN_PARAMS_PATH)
        self.goto_exercise_handler = goto_foreign_exercise_handler
        self.goto_table_handler = goto_foreign_table_handler


class ExerciseForeignPage(ExerciseLayout):
    """Foreign exercise page."""

    title = TITLE_FOREIGN_EXERCISE

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self.plc.url_exercise = urljoin(HOST, FOREIGN_EXERCISE_PATH)
        self.plc.url_progress = urljoin(HOST, FOREIGN_ASSESSMENT_PATH)
        self.plc.url_favorites = urljoin(HOST, FOREIGN_FAVORITES_PATH)


class CreateWordPage(ForeignFormLayout):
    """Add word to foreign dictionary."""

    title = TITLE_FOREIGN_CREATE
    url = urljoin(HOST, FOREIGN_PATH)
    submit_text = 'Добавить'
    accessors = ACCESSORS


class UpdateWordPage(ForeignFormLayout):
    """Update the foreign word the box."""

    title = TITLE_FOREIGN_UPDATE
    url = urljoin(HOST, FOREIGN_DETAIL_PATH)
    submit_text = 'Изменить'
    accessors = ACCESSORS


class TableForeignPage(TableLayout):
    """Table of list of foreign words."""

    title = TITLE_FOREIGN_LIST
    url = urljoin(HOST, FOREIGN_SELECTED_PATH)
    url_detail = urljoin(HOST, FOREIGN_DETAIL_PATH)
    table_headings = ['На иностранном', 'На родном']
    table_accessors = ['foreign_word', 'native_word']
    source_accessors = ACCESSORS

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self._plc.goto_create_handler = goto_foreign_create_handler
        self._plc.goto_update_handler = goto_foreign_update_handler
