"""The page to explore Toga widgets."""

from tkinter.constants import CENTER

import toga
from toga import colors
from toga.constants import COLUMN
from toga.style import Pack

from wse.handlers.goto_handler import goto_back_handler
from wse.widgets.button import BtnApp


class Explorer(toga.Box):
    """The page to explore Toga widgets."""

    def __init__(self) -> None:
        """Construct the widgets."""
        super().__init__()

        self.title = toga.Label(
            text='Страница изучения виджетов.',
            style=Pack(text_align=CENTER),
        )

        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)


class ExplorerLayout(Explorer):
    """Layout of explorer page."""

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()
        self.style.direction = COLUMN

        self.create_widgets()

        # DOM
        self.add(
            self.box_title,
            self.btn_goto_back,
        )

    def create_widgets(self) -> None:
        """Run create widgets."""
        self.create_title_box()

    def create_title_box(self) -> None:
        """Create title box."""
        self.box_title = toga.Box(
            style=Pack(
                background_color=colors.GREEN,
                direction=COLUMN,
            ),
            children=[self.title],
        )
