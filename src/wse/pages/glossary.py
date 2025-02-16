"""Glossary pages."""

from urllib.parse import urljoin

from toga.style import Pack

from wse import constants as const
from wse.constants.settings import TEXT_DISPLAY_FONT_SIZE
from wse.controllers.form import TermFormController
from wse.pages.base import BasePage
from wse.pages.containers.exercise import ExerciseLayout
from wse.pages.containers.form import FormLayout
from wse.pages.containers.params import ParamsLayout
from wse.pages.containers.table import TableLayout
from wse.pages.handlers.goto_handler import (
    goto_glossary_create,
    goto_glossary_exercise_handler,
    goto_glossary_selected_handler,
    goto_glossary_update_handler,
)
from wse.pages.widgets import BoxFlexCol
from wse.pages.widgets.box_page import WidgetMixin
from wse.pages.widgets.button import BtnApp, BtnBack
from wse.pages.widgets.text import InputTextField

ACCESSORS = ['id', 'term', 'definition']


class MainGlossaryWidget(WidgetMixin, BasePage):
    """Glossary main box."""

    title = 'Глоссарий'

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()

        # Buttons
        self._btn_goto_params = BtnApp(**self._nav.glossary_params)
        self._btn_goto_create = BtnApp(**self._nav.glossary_create)
        self._btn_goto_back = BtnBack()

        # DOM
        self.add(
            BoxFlexCol(),
            self._btn_goto_create,
            self._btn_goto_params,
            self._btn_goto_back,
        )


class ParamsGlossaryPage(ParamsLayout):
    """Glossary exercise params pages."""

    title = const.TITLE_GLOSSARY_PARAMS
    url = urljoin(const.HOST, const.GLOSSARY_PARAMS_PATH)
    goto_exercise_handler = goto_glossary_exercise_handler
    goto_table_handler = goto_glossary_selected_handler


class ExerciseGlossaryPage(ExerciseLayout):
    """Glossary exercise pages."""

    title = const.TITLE_GLOSSARY_EXERCISE
    url_exercise = urljoin(const.HOST, const.GLOSSARY_EXERCISE_PATH)
    url_progress = urljoin(const.HOST, const.GLOSSARY_PROGRESS_PATH)
    url_favorites = urljoin(const.HOST, const.GLOSSARY_FAVORITES_PATH)

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the pages."""
        super().__init__(*args, **kwargs)
        self._text_panel_question.style.flex = 1
        self._text_panel_answer.style.flex = 5
        self._text_panel_answer.style.font_size = 12


class TermForm(FormLayout):
    """Term form container."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the form."""
        super().__init__(*args, **kwargs)

        # Term data input widgets
        self._input_term = InputTextField(
            style=Pack(
                flex=1,
                font_size=TEXT_DISPLAY_FONT_SIZE,
                padding_bottom=1,
            ),
            placeholder='Термин',
            on_change=self._plc.term.change,
        )
        self._input_definition = InputTextField(
            style=Pack(
                flex=4,
                font_size=16,
            ),
            placeholder='Определение',
            on_change=self._plc.definition.change,
        )

        # Update DOM
        self.insert(1, self._input_term)
        self.insert(2, self._input_definition)

    #####################################################################
    # Notification methods

    def populate_form(self, data: TermFormController) -> None:
        """Set initial values for form input widgets."""
        self._input_term.value = data.term.value
        self._input_definition.value = data.definition.value

    def clear_form(self) -> None:
        """Clear the form."""
        self._input_term.value = ''
        self._input_definition.value = ''

    #####################################################################
    # Interactive methods

    def _focus_to_input_field(self) -> None:
        self._input_term.focus()


class CreateTermPage(TermForm):
    """Term create pages."""

    title = const.TITLE_GLOSSARY_CREATE
    url = urljoin(const.HOST, const.GLOSSARY_PATH)
    submit_text = 'Добавить'
    accessors = ACCESSORS


class UpdateTermPage(TermForm):
    """Term update pages."""

    title = const.TITLE_GLOSSARY_UPDATE
    url = urljoin(const.HOST, const.GLOSSARY_DETAIL_PATH)
    submit_text = 'Изменить'
    accessors = ACCESSORS


class TableTermPage(TableLayout):
    """Term list table pages."""

    title = const.TITLE_GLOSSARY_LIST
    url = urljoin(const.HOST, const.GLOSSARY_SELECTED_PATH)
    url_detail = urljoin(const.HOST, const.GLOSSARY_DETAIL_PATH)
    table_headings = ['Термин', 'Толкование']
    table_accessors = ['term', 'definition']
    source_accessors = ACCESSORS

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the pages."""
        super().__init__(*args, **kwargs)
        self._plc.goto_create_handler = goto_glossary_create
        self._plc.goto_update_handler = goto_glossary_update_handler
