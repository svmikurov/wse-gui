"""Base pages."""

from typing import TypeVar

import toga
from toga.constants import COLUMN
from toga.sources import Listener

from wse.constants.settings import PADDING_SM
from wse.controllers.nav import Navigation
from wse.pages.widgets.label import TitleLabel

ContrT = TypeVar('ContrT', bound=Listener)


class BasePage(toga.Box):
    """Base pages."""

    title: str | None = None

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()
        self.style.direction = COLUMN
        self.style.padding = PADDING_SM
        self.style.flex = 1

        # Controllers
        self._controller: ContrT | None = None

        # Base page has button controller to move to pages.
        self._nav = Navigation()

        if self.title:
            self._label_title = TitleLabel(text=self.title)
            self.add(self._label_title)

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on pages open."""
        await self._controller.on_open(widget)

    def set_controller(self, controller: ContrT) -> None:
        """Set the view controller."""
        self._controller = controller
