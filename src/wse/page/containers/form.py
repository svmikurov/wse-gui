"""Form container."""

from typing import TypeVar

import toga

from wse.page.handlers.goto_handler import goto_back_handler
from wse.page.widgets.box_page import BaseBox
from wse.page.widgets.button import BtnApp
from wse.page.widgets.label import TitleLabel

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
        raise NotImplementedError(
            '`_focus_to_input_field()` must be implemented.'
        )


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
