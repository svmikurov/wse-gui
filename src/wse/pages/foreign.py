"""Foreign words page boxes."""

from http import HTTPStatus
from urllib.parse import urljoin

import toga
from httpx import Response
from toga.style import Pack

from wse.constants import (
    BTN_GOTO_FOREIGN_CREATE,
    BTN_GOTO_FOREIGN_LIST,
    BTN_GOTO_FOREIGN_PARAMS,
    FOREIGN_ASSESSMENT_PATH,
    FOREIGN_DETAIL_PATH,
    FOREIGN_EXERCISE_PATH,
    FOREIGN_FAVORITES_PATH,
    FOREIGN_PARAMS_PATH,
    FOREIGN_PATH,
    FOREIGN_PATH_SELECTED,
    HOST,
    TITLE_FOREIGN_CREATE,
    TITLE_FOREIGN_EXERCISE,
    TITLE_FOREIGN_LIST,
    TITLE_FOREIGN_MAIN,
    TITLE_FOREIGN_PARAMS,
    TITLE_FOREIGN_UPDATE,
)
from wse.contrib.http_requests import (
    request_post_async,
    request_put_async,
)
from wse.pages.containers.exercise import (
    ExerciseLayout,
)
from wse.pages.containers.params import ParamsLayout
from wse.pages.containers.table import TableLayout
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_foreign_create_handler,
    goto_foreign_exercise_handler,
    goto_foreign_params_handler,
    goto_foreign_selected_handler,
    goto_foreign_update_handler,
)
from wse.pages.widgets.box_page import BaseBox, WidgetMixin
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.form import BaseForm
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import MulTextInpApp
from wse.sources.foreign import Word, WordSource


class MainForeignPage(WidgetMixin, BaseBox):
    """Learning foreign words the main page box."""

    def __init__(self) -> None:
        """Construct the box."""
        super().__init__()

        # fmt: off
        # Box widgets
        self.label_title = TitleLabel(TITLE_FOREIGN_MAIN)
        self.btn_goto_params = BtnApp(BTN_GOTO_FOREIGN_PARAMS, on_press=goto_foreign_params_handler)  # noqa: E501
        self.btn_goto_create = BtnApp(BTN_GOTO_FOREIGN_CREATE, on_press=goto_foreign_create_handler)  # noqa: E501
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


class ParamsForeignPage(ParamsLayout):
    """Learning foreign words exercise parameters the page box."""

    title = TITLE_FOREIGN_PARAMS

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self.plc.url = urljoin(HOST, FOREIGN_PARAMS_PATH)
        self.goto_exercise_handler = goto_foreign_exercise_handler
        self.goto_selected_handler = goto_foreign_selected_handler


class ExerciseForeignPage(ExerciseLayout):
    """Foreign exercise page."""

    title = TITLE_FOREIGN_EXERCISE

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self.plc.url_exercise = urljoin(HOST, FOREIGN_EXERCISE_PATH)
        self.plc.url_progress = urljoin(HOST, FOREIGN_ASSESSMENT_PATH)
        self.plc.url_favorites = urljoin(HOST, FOREIGN_FAVORITES_PATH)
        self.plc.exercise_page = self


class FormForeign(BaseBox, BaseForm):
    """General form to create and update entries, the container."""

    title = ''

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the foreign form."""
        super().__init__(*args, **kwargs)
        self._entry = Word

        self.label_title = TitleLabel(text=self.title)

        # fmt: off
        # Word data input widgets
        self.input_native = MulTextInpApp(placeholder='Слово на русском')
        self.input_native.style.padding_bottom = 1
        self.input_foreign = MulTextInpApp(placeholder='Слово на иностранном')
        self.btn_submit = BtnApp(self.btn_submit_text, on_press=self.submit_handler)  # noqa: E501
        # Buttons
        self.btn_goto_foreign_list = BtnApp(BTN_GOTO_FOREIGN_LIST, on_press=goto_foreign_selected_handler)  # noqa: E501
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

        # DOM
        self.add(
            self.label_title,
            self.input_native,
            self.input_foreign,
            self.btn_submit,
            self.btn_goto_foreign_list,
            self.btn_goto_back,
        )

    def populate_entry_input(self) -> None:
        """Populate the entry input widgets value."""
        self.input_native.value = self.entry.native_word
        self.input_foreign.value = self.entry.foreign_word

    def clear_entry_input(self) -> None:
        """Clear the entry input widgets value."""
        self.input_native.clean()
        self.input_foreign.clean()

    def focus_to_input_field(self) -> None:
        """Focus to input field."""
        self.input_native.focus()


class CreateWordPage(FormForeign):
    """Add word to foreign dictionary."""

    title = TITLE_FOREIGN_CREATE
    url = urljoin(HOST, FOREIGN_PATH)
    btn_submit_text = 'Добавить'
    success_http_status = HTTPStatus.CREATED

    def get_widget_data(self) -> dict:
        """Get the entered into the form data."""
        entry_create = {
            'foreign_word': self.input_foreign.value,
            'native_word': self.input_native.value,
        }
        return entry_create

    @classmethod
    async def request_async(cls, url: str, payload: dict) -> Response:
        """Request to update."""
        return await request_post_async(url, payload)

    async def handle_success(self, widget: toga.Widget) -> None:
        """Go to foreign list page, if success."""
        self.focus_to_input_field()


class UpdateWordPage(FormForeign):
    """Update the foreign word the box."""

    title = TITLE_FOREIGN_UPDATE
    url = urljoin(HOST, FOREIGN_DETAIL_PATH)
    btn_submit_text = 'Изменить'
    success_http_status = HTTPStatus.OK

    def get_widget_data(self) -> dict:
        """Get the entered into the form data."""
        entry_updated = {
            'id': str(self.entry.id),
            'foreign_word': self.input_foreign.value,
            'native_word': self.input_native.value,
        }
        return entry_updated

    @classmethod
    async def request_async(cls, url: str, payload: dict) -> Response:
        """Request to update."""
        return await request_put_async(url, payload)

    async def handle_success(self, widget: toga.Widget) -> None:
        """Go to foreign list page, if success."""
        await goto_foreign_selected_handler(widget)


class SelectedForeignPage(TableLayout):
    """Table of list of foreign words."""

    title = TITLE_FOREIGN_LIST
    source_class = WordSource()

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self.plc.source_url = urljoin(HOST, FOREIGN_PATH_SELECTED)
        self.plc.source_url_detail = urljoin(HOST, FOREIGN_DETAIL_PATH)
        self.plc.headings = ['Иностранный', 'Русский']

    async def create_handler(self, widget: toga.Widget) -> None:
        """Go to create the word form, button handler."""
        await goto_foreign_create_handler(widget)

    async def update_handler(self, widget: toga.Widget) -> None:
        """Go to update the word form, button handler."""
        entry = self._table.selection
        box = self.root.app.box_foreign_update
        box.entry = entry
        await goto_foreign_update_handler(widget)
