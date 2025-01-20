"""Glossary page boxes."""

from urllib.parse import urljoin

import toga
from toga.style import Pack

from wse.constants import (
    BTN_GOTO_GLOSSARY_CREATE,
    BTN_GOTO_GLOSSARY_PARAMS,
    GLOSSARY_DETAIL_PATH,
    GLOSSARY_PARAMS_PATH,
    GLOSSARY_PATH,
    HOST,
    TITLE_GLOSSARY_CREATE,
    TITLE_GLOSSARY_EXERCISE, TITLE_GLOSSARY_LIST,
    TITLE_GLOSSARY_MAIN,
    TITLE_GLOSSARY_PARAMS,
    TITLE_GLOSSARY_UPDATE,
)
from wse.constants.url import GLOSSARY_EXERCISE_PATH, GLOSSARY_FAVORITES_PATH, \
    GLOSSARY_PROGRESS_PATH, \
    GLOSSARY_SELECTED_PATH
from wse.pages.containers.exercise import ExerciseLayout
from wse.pages.containers.form import GlossaryFormLayout
from wse.pages.containers.params import ParamsLayout
from wse.pages.containers.table import TableLayout
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_glossary_create_handler,
    goto_glossary_exercise_handler,
    goto_glossary_params_handler,
    goto_glossary_selected_handler,
    goto_glossary_update_handler,
)
from wse.pages.widgets.box_page import (
    BaseBox,
    WidgetMixin,
)
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel

ACCESSORS = ['id', 'term', 'definition']


class MainGlossaryWidget(WidgetMixin, BaseBox):
    """Glossary main box."""

    def __init__(self) -> None:
        """Construct the box."""
        super().__init__()

        # fmt: off
        # Box widgets.
        self.label_title = TitleLabel(TITLE_GLOSSARY_MAIN)
        self.btn_goto_params = BtnApp(BTN_GOTO_GLOSSARY_PARAMS, on_press=goto_glossary_params_handler)  # noqa: E501
        self.btn_goto_create = BtnApp(BTN_GOTO_GLOSSARY_CREATE, on_press=goto_glossary_create_handler)  # noqa: E501
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

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


class ParamsGlossaryPage(ParamsLayout):
    """Glossary page box."""

    title = TITLE_GLOSSARY_PARAMS

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self.plc.url = urljoin(HOST, GLOSSARY_PARAMS_PATH)
        self.goto_exercise_handler = goto_glossary_exercise_handler
        self.goto_table_handler = goto_glossary_selected_handler


class ExerciseGlossaryPage(ExerciseLayout):
    """Glossary exercise page."""

    title = TITLE_GLOSSARY_EXERCISE

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self.plc.url_exercise = urljoin(HOST, GLOSSARY_EXERCISE_PATH)
        self.plc.url_progress = urljoin(HOST, GLOSSARY_PROGRESS_PATH)
        self.plc.url_favorites = urljoin(HOST, GLOSSARY_FAVORITES_PATH)


class CreateTermPage(GlossaryFormLayout):
    """Glossary create page."""

    title = TITLE_GLOSSARY_CREATE
    url = urljoin(HOST, GLOSSARY_PATH)
    submit_text = 'Добавить'
    accessors = ACCESSORS


class UpdateTermPage(GlossaryFormLayout):
    """Glossary update page."""

    title = TITLE_GLOSSARY_UPDATE
    url = urljoin(HOST, GLOSSARY_DETAIL_PATH)
    submit_text = 'Изменить'
    accessors = ACCESSORS


class TableTermPage(TableLayout):
    """Table of list of glossary terms, the page."""

    title = TITLE_GLOSSARY_LIST
    url = urljoin(HOST, GLOSSARY_SELECTED_PATH)
    url_detail = urljoin(HOST, GLOSSARY_DETAIL_PATH)
    table_headings = ['Термин', 'Толкование']
    table_accessors = ['term', 'definition']
    source_accessors = ACCESSORS

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self._plc.goto_create_handler = goto_glossary_create_handler
        self._plc.goto_update_handler = goto_glossary_update_handler
