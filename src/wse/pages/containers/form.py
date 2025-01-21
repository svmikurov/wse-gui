"""Form container."""

from typing import TypeVar

import toga
from toga.style import Pack

from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import MulTextInpApp

T = TypeVar('T')


class FormWidgets:
    """Form widgets."""

    title: str
    submit_text: str
    accessors: list
    url: str

    def __init__(self, controller: T) -> None:
        """Construct the form."""
        super().__init__()
        self._plc = controller
        self._plc.accessors = self.accessors
        self._plc.add_listener(self)

        self._label_title = TitleLabel(text=self.title)

        # Buttons
        self._btn_submit = BtnApp(
            self.submit_text,
            on_press=self._submit_handler,
        )
        self._btn_goto_back = BtnApp(
            'Назад',
            on_press=goto_back_handler,
        )

    async def on_open(self, *args: object, **kwargs: object) -> None:
        """Populate the widgets."""
        self._focus_to_input_field()
        await self._plc.on_open(*args, **kwargs)

    #####################################################################
    # Button handlers

    async def _submit_handler(self, widget: toga.Widget) -> None:
        await self._plc.submit_handler(widget, self.url)
        self._focus_to_input_field()

    #####################################################################
    # Interactive methods

    def _focus_to_input_field(self) -> None:
        raise NotImplementedError()


class FormLayout(FormWidgets, BaseBox):
    """Layout of form."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the container."""
        super().__init__(*args, **kwargs)

        self.add(
            self._label_title,
            self._btn_submit,
            self._btn_goto_back,
        )


class ForeignFormWidgets(FormWidgets):
    """Foreign form widgets."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widgets."""
        super().__init__(*args, **kwargs)

        # Word data input widgets
        self._input_native = MulTextInpApp(
            style=Pack(padding_bottom=1),
            placeholder='Слово на русском',
            on_change=self._plc.native_word.change,
        )
        self._input_foreign = MulTextInpApp(
            placeholder='Слово на иностранном',
            on_change=self._plc.foreign_word.change,
        )

    #####################################################################
    # Notification methods

    def populate_form(self, data: T) -> None:
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


class ForeignFormLayout(ForeignFormWidgets, FormLayout):
    """Foreign form layout."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the container."""
        super().__init__(*args, **kwargs)
        # Add specific fields
        self.insert(1, self._input_foreign)
        self.insert(2, self._input_native)


class GlossaryFormWidgets(FormWidgets):
    """Glossary form widgets."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widgets."""
        super().__init__(*args, **kwargs)

        # Word data input widgets
        self._input_term = MulTextInpApp(
            style=Pack(padding_bottom=1),
            placeholder='Термин',
            on_change=self._plc.term.change,
        )
        self._input_definition = MulTextInpApp(
            placeholder='Определение',
            on_change=self._plc.definition.change,
        )

    #####################################################################
    # Notification methods

    def populate_form(self, data: T) -> None:
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


class GlossaryFormLayout(GlossaryFormWidgets, FormLayout):
    """Glossary form layout."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the container."""
        super().__init__(*args, **kwargs)
        # Add specific fields
        self.insert(1, self._input_term)
        self.insert(2, self._input_definition)
