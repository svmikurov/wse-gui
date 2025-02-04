"""Fraction exercise container."""

from wse.page.handlers.goto_handler import goto_back_handler
from wse.page.widgets.box import BoxFlexRow
from wse.page.widgets.box_page import BaseBox
from wse.page.widgets.button import BtnApp
from wse.page.widgets.label import TitleLabel


class FractionWidgets:
    """Fraction exercise widgets."""

    title: str

    def __init__(self, controller: object | None = None) -> None:
        """Construct the widgets."""
        super().__init__()
        self._plc = controller

        self._label_title = TitleLabel(text=self.title)
        self._box_align = BoxFlexRow()
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)


class FractionLayout(FractionWidgets, BaseBox):
    """Fraction exercise layout."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the layout."""
        super().__init__(*args, **kwargs)

        self.add(
            self._label_title,
            self._box_align,
            self._btn_goto_back,
        )
