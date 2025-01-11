"""Glossary page boxes."""

from http import HTTPStatus
from urllib.parse import urljoin

import toga
from httpx import Response

from wse.constants import (
    BTN_GOTO_GLOSSARY_CREATE,
    BTN_GOTO_GLOSSARY_LIST,
    BTN_GOTO_GLOSSARY_PARAMS,
    GLOSSARY_DETAIL_PATH,
    GLOSSARY_EXERCISE_PATH,
    GLOSSARY_PARAMS_PATH,
    GLOSSARY_PATH,
    GLOSSARY_PROGRESS_PATH,
    HOST,
    TITLE_GLOSSARY_CREATE,
    TITLE_GLOSSARY_EXERCISE,
    TITLE_GLOSSARY_LIST,
    TITLE_GLOSSARY_MAIN,
    TITLE_GLOSSARY_PARAMS,
    TITLE_GLOSSARY_UPDATE,
)
from wse.contrib.http_requests import (
    HttpPostMixin,
    request_post_async,
    request_put_async,
)
from wse.pages.containers.exercise import ExerciseLayout
from wse.pages.containers.params import ParamsLayout
from wse.pages.containers.table import TableLayout
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_glossary_create_handler,
    goto_glossary_list_handler,
    goto_glossary_params_handler,
    goto_glossary_update_handler,
)
from wse.pages.widgets.box_page import (
    BaseBox,
    WidgetMixin,
)
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.form import BaseForm
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import MulTextInpApp
from wse.sources.glossary import Term, TermSource


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
        self.btn_goto_list = BtnApp(BTN_GOTO_GLOSSARY_LIST, on_press=goto_glossary_list_handler)  # noqa: E501
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

        # Widget DOM.
        self.add(
            self.label_title,
            self.btn_goto_params,
            self.btn_goto_create,
            self.btn_goto_list,
            self.btn_goto_back,
        )


class ParamsGlossaryPage(ParamsLayout):
    """Glossary page box."""

    title = TITLE_GLOSSARY_PARAMS

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self.plc.url = urljoin(HOST, GLOSSARY_PARAMS_PATH)


class ExerciseGlossaryPage(ExerciseLayout):
    """Glossary exercise page."""

    title = TITLE_GLOSSARY_EXERCISE

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self.url_exercise = urljoin(HOST, GLOSSARY_EXERCISE_PATH)
        self.url_progress = urljoin(HOST, GLOSSARY_PROGRESS_PATH)


class FormGlossary(BaseBox, BaseForm):
    """General form to create and update entries, the container."""

    title = ''

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the glossary form."""
        super().__init__(*args, **kwargs)
        self._entry = Term

        self.label_title = TitleLabel(text=self.title)

        # fmt: off
        # Term data input widgets
        self.input_term = MulTextInpApp(placeholder='Термин')
        self.input_term.style.padding_bottom = 1
        self.input_definition = MulTextInpApp(placeholder='Определение')
        self.btn_submit = BtnApp(self.btn_submit_text, on_press=self.submit_handler)  # noqa: E501
        # Buttons
        self.btn_goto_glossary_list = BtnApp(BTN_GOTO_GLOSSARY_LIST, on_press=goto_glossary_list_handler)  # noqa: E501
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

        self.add(
            self.label_title,
            self.input_term,
            self.input_definition,
            self.btn_submit,
            self.btn_goto_glossary_list,
            self.btn_goto_back,
        )

    def populate_entry_input(self) -> None:
        """Populate the entry input widgets value."""
        self.input_term.value = self.entry.term
        self.input_definition.value = self.entry.definition

    def clear_entry_input(self) -> None:
        """Clear the entry input widgets value."""
        self.input_term.clean()
        self.input_definition.clean()

    def focus_to_input_field(self) -> None:
        """Focus to input field."""
        self.input_term.focus()


class CreateTermPage(HttpPostMixin, FormGlossary):
    """Glossary create page."""

    title = TITLE_GLOSSARY_CREATE
    url = urljoin(HOST, GLOSSARY_PATH)
    btn_submit_text = 'Добавить'
    success_http_status = HTTPStatus.CREATED

    def get_widget_data(self) -> dict:
        """Get the entered into the form data."""
        entry_create = {
            'term': self.input_term.value,
            'definition': self.input_definition.value,
        }
        return entry_create

    @classmethod
    async def request_async(cls, url: str, payload: dict) -> Response:
        """Request to update."""
        return await request_post_async(url, payload)

    async def handle_success(self, widget: toga.Widget) -> None:
        """Go to glossary list page, if success."""
        self.focus_to_input_field()


class UpdateTermPage(FormGlossary):
    """Glossary update page."""

    title = TITLE_GLOSSARY_UPDATE
    url = urljoin(HOST, GLOSSARY_DETAIL_PATH)
    btn_submit_text = 'Изменить'
    success_http_status = HTTPStatus.OK

    def get_widget_data(self) -> dict:
        """Get the entered into the form data."""
        entry_updated = {
            'id': str(self.entry.id),
            'term': self.input_term.value,
            'definition': self.input_definition.value,
        }
        return entry_updated

    @classmethod
    async def request_async(cls, url: str, payload: dict) -> Response:
        """Request to update."""
        return await request_put_async(url, payload)

    @classmethod
    async def handle_success(cls, widget: toga.Widget) -> None:
        """Go to glossary list page, if success."""
        await goto_glossary_list_handler(widget)


class ListGlossaryPage(TableLayout):
    """Table of list of glossary terms, the page."""

    title = TITLE_GLOSSARY_LIST
    source_class = TermSource()
    source_url = urljoin(HOST, GLOSSARY_PATH)
    source_url_detail = urljoin(HOST, GLOSSARY_DETAIL_PATH)
    headings = ['ID', 'Термин', 'Толкование']

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()

    async def create_handler(self, widget: toga.Widget) -> None:
        """Go to create the term form, button handler."""
        await goto_glossary_create_handler(widget)

    async def update_handler(self, widget: toga.Widget) -> None:
        """Go to update the term form, button handler."""
        entry = self.table.selection
        box = self.root.app.box_glossary_update
        box.entry = entry
        await goto_glossary_update_handler(widget)
