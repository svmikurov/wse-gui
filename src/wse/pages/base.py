"""Base pages."""

from typing import Callable

import toga

from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.label import TitleLabel


class BasePage(BaseBox):
    """Base pages."""

    title: str | None = None

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()
        self.on_open_func: Callable | None = None

        if self.title:
            _label_title = TitleLabel(text=self.title)

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on pages open."""
        await self.on_open_func(widget)
