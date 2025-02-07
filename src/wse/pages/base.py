"""Base pages."""

from typing import TypeVar

import toga
from toga.constants import COLUMN
from toga.sources import Listener

from wse.constants.settings import PADDING_SM
from wse.controllers.nav import Navigation
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import UserInfoPanel

ContrT = TypeVar('ContrT', bound=Listener)


class BasePage(toga.Box):
    """Base pages."""

    title: str | None = None

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()
        # Page style
        self.style.direction = COLUMN
        self.style.padding = PADDING_SM
        self.style.flex = 1

        # Controllers
        self._contr: ContrT | None = None
        # Base page has button controller to move to pages.
        self._nav = Navigation()

        # User data panel
        self.user_info_panel = UserInfoPanel()

        # DOM
        self.insert(0, self.user_info_panel)
        if self.title:
            self._label_title = TitleLabel(text=self.title)
            self.add(self._label_title)

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on pages open."""
        pass

    def set_controller(self, contr: ContrT) -> None:
        """Set the view controller."""
        self._contr = contr
