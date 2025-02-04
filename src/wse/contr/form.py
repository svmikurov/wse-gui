"""Form controller."""

import toga
from toga.sources import Source, ValueSource

from wse.contrib.http_requests import (
    request_create_async,
    request_data_async,
    request_update_async,
)
from wse.page.handlers.goto_handler import goto_back_handler


class TextInputSource(ValueSource):
    """Source for text input widgets."""

    def __init__(self, value: str = '', accessor: str = 'value') -> None:
        """Construct the source."""
        super().__init__(value, accessor)

    def change(self, widget: toga.MultilineTextInput | toga.TextInput) -> None:
        """Change source value by widget."""
        setattr(self, self.accessor, widget.value)

    def set_value(self, value: str) -> None:
        """Set value to source by controller."""
        setattr(self, self.accessor, value)


class FormController(Source):
    """Form controller."""

    id: TextInputSource  # sets dynamically by form_data property

    def __init__(self) -> None:
        """Construct the controller."""
        super().__init__()
        self.accessors = []

    async def on_open(
        self,
        _: toga.Widget,
        url: str | None = None,
        item_id: str | None = None,
    ) -> None:
        """Populate the widget values."""
        if item_id:
            # The form is used for updating, otherwise for creating.
            url = url % item_id
            data = await request_data_async(url)
            self._update_sources(data)
            self._populate_form()

    #####################################################################
    # Notifications

    def _populate_form(self) -> None:
        """Populate form widgets."""
        self.notify('populate_form', data=self)

    def _clear_form(self) -> None:
        self.notify('clear_form')

    #####################################################################
    # Button handlers

    async def submit_handler(self, widget: toga.Widget, url: str) -> None:
        """Submit form data."""
        if '%' in url:
            await request_update_async(url % self.id, self.form_data)
            self._clear()
            await goto_back_handler(widget)
        else:
            await request_create_async(url, self.form_data)
            self._clear()

    #################
    # Utility methods

    def _clear(self) -> None:
        self._clear_sources()
        self._clear_form()

    #####################################################################
    # Source methods

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


class WordFormController(FormController):
    """Foreign form controller."""

    def __init__(self) -> None:
        """Construct the controller."""
        super().__init__()
        self.id = TextInputSource()
        self.native_word = TextInputSource()
        self.foreign_word = TextInputSource()


class TermFormController(FormController):
    """Glossary form controller."""

    def __init__(self) -> None:
        """Construct the controller."""
        super().__init__()
        self.id = TextInputSource()
        self.term = TextInputSource()
        self.definition = TextInputSource()
