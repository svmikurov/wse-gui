"""Base page."""

from typing import Callable

import toga

from wse.page.widgets.box_page import BaseBox
from wse.page.widgets.label import TitleLabel


class BasePage(BaseBox):
    """Base page."""

    title: str | None = None

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()
        self.on_open_func: Callable | None = None

        if self.title:
            _label_title = TitleLabel(text=self.title)

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        await self.on_open_func(widget)
