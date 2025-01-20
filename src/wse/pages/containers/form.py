"""Form container."""

from toga.style import Pack

from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import MulTextInpApp


class FormWidgets:
    """Form container widgets."""

    title: str
    submit_text: str
    input_native: MulTextInpApp
    input_foreign: MulTextInpApp
    accessors: list

    def __init__(self, controller: object) -> None:
        """Construct the form."""
        super().__init__()
        self.plc = controller
        self.plc.accessors = self.accessors
        self.plc.add_listener(self)

        self.label_title = TitleLabel(text=self.title)

        # Word data input widgets
        self.input_native = MulTextInpApp(
            style=Pack(padding_bottom=1),
            placeholder='Слово на русском',
            on_change=self.plc.native_word.change,
        )
        self.input_foreign = MulTextInpApp(
            placeholder='Слово на иностранном',
            on_change=self.plc.foreign_word.change,
        )
        # Buttons
        self.btn_submit = BtnApp(self.submit_text, on_press=self.plc.submit)
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

    async def on_open(self, *args: object, **kwargs: object) -> None:
        """Populate the widgets."""
        await self.plc.on_open(*args, **kwargs)

    #####################################################################
    # Notification methods

    def populate_form(self, data: object) -> None:
        """Set initial values for form input widgets."""
        self.input_native.value = data.native_word.value
        self.input_foreign.value = data.foreign_word.value

    def clear_form(self) -> None:
        """Clear the form."""
        self.input_native.value = ''
        self.input_foreign.value = ''


class FormLayout(FormWidgets, BaseBox):
    """Layout of form."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the container."""
        super().__init__(*args, **kwargs)

        self.add(
            self.label_title,
            self.input_foreign,
            self.input_native,
            self.btn_submit,
            self.btn_goto_back,
        )
