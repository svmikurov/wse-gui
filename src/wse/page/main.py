"""Main box."""

import toga
from toga.style import Pack

from wse.constants import (
    BTN_GOTO_FOREIGN_MAIN,
    BTN_GOTO_GLOSSARY_MAIN,
    FOREIGN_MAIN_BOX,
    GLOSSARY_MAIN_BOX,
    HOST_API,
    TITLE_MAIN,
)
from wse.general.box_page import BoxApp
from wse.general.button import BtnApp
from wse.general.label import TitleLabel
from wse.page.user import UserAuth


class MainBox(UserAuth, BoxApp):
    """Main box.

    Contains content that is displayed to the user
    when the application is launched.
    """

    welcome = f'Ready for connect to {HOST_API}'
    """Welcome text on the information display (`str`).
    """

    def __init__(self) -> None:
        """Construct the Main box."""
        super().__init__()

        # Widgets.
        self.label_title = TitleLabel(TITLE_MAIN)
        self.btn_goto_glossary_main = BtnApp(
            BTN_GOTO_GLOSSARY_MAIN,
            on_press=lambda _: self.goto_box_handler(_, GLOSSARY_MAIN_BOX),  # noqa: E501
        )
        self.btn_goto_foreign_main = BtnApp(
            BTN_GOTO_FOREIGN_MAIN,
            on_press=lambda _: self.goto_box_handler(_, FOREIGN_MAIN_BOX),  # noqa: E501
        )

        # Info panel
        self.info_panel = toga.MultilineTextInput(
            readonly=True,
            placeholder=self.welcome,
            style=Pack(flex=1),
        )

        # DOM.
        self.add(
            self.label_title,
            self.btn_goto_auth,  # UserAuth attr
            self.btn_goto_foreign_main,
            self.btn_goto_glossary_main,
            self.info_panel,
        )
