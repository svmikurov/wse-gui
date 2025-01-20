"""Form controller."""

from http import HTTPStatus

import toga
from toga.sources import Source, ValueSource

from wse.contrib.http_requests import request_get_async, request_put_async
from wse.pages.handlers.goto_handler import goto_back_handler


class TextInputSource(ValueSource):
    """Source for text input widgets."""

    def __init__(self, value: str = '', accessor: str = 'value') -> None:
        """Construct the source."""
        super().__init__(value, accessor)

    def change(self, widget: toga.MultilineTextInput | toga.TextInput) -> None:
        """Change source value."""
        setattr(self, self.accessor, widget.value)

    def set_value(self, value: str) -> None:
        """Set value to source."""
        setattr(self, self.accessor, value)


class FormController(Source):
    """Form controller."""

    url: str
    id: TextInputSource

    def __init__(self) -> None:
        """Construct the controller."""
        super().__init__()
        self.accessors = []

    async def on_open(
        self, _: toga.Widget, item_id: str | None = None
    ) -> None:
        """Populate the widget values."""
        url = self.url % item_id
        data = await self._request_data(url)
        self._update_sources(data)
        self._populate_form()

    #####################################################################
    # Button handlers

    async def submit(self, widget: toga.Widget) -> None:
        """Submit form data."""
        url = self.url % self.id
        await self._request_update(url, self.form_data)
        self._clear_sources()
        self._clear_form()
        await goto_back_handler(widget)

    #####################################################################
    # Source

    def _update_sources(self, data: dict) -> None:
        """Update form sources."""
        for name, value in data.items():
            if name not in self.accessors:
                raise ValueError('There is no such accessor')
            source = getattr(self, name)
            source.set_value(value)

    def _clear_sources(self) -> None:
        for accessor in self.accessors:
            source = getattr(self, accessor)
            source.value = ''

    @property
    def form_data(self) -> dict:
        """Data from form."""
        data = {}
        for accessor in self.accessors:
            source = getattr(self, accessor)
            data[accessor] = source.value
        return data

    #####################################################################
    # Notifications

    def _populate_form(self) -> None:
        """Populate form widgets."""
        self.notify('populate_form', data=self)

    def _clear_form(self) -> None:
        self.notify('clear_form')

    #####################################################################
    # Http requests

    @staticmethod
    async def _request_data(url: str) -> dict:
        """Request item data."""
        response = await request_get_async(url)
        if response.status_code == HTTPStatus.OK:
            data = response.json()
            return data

    @staticmethod
    async def _request_update(url: str, payload: dict) -> None:
        await request_put_async(url, payload=payload)


class ForeignFormController(FormController):
    """Foreign form controller."""

    def __init__(self) -> None:
        """Construct the controller."""
        super().__init__()
        self.id = TextInputSource()
        self.native_word = TextInputSource()
        self.foreign_word = TextInputSource()


class GlossaryFormController(FormController):
    """Glossary form controller."""

    def __init__(self) -> None:
        """Construct the controller."""
        super().__init__()
        self.id = TextInputSource()
        self.term = TextInputSource()
        self.definition = TextInputSource()
