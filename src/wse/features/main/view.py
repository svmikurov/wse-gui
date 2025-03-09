"""Defines the main screen view."""

import toga
from toga.sources import Source

from wse.features.shared.ui.box import ColumnFlexBox
from wse.features.shared.ui.button import ButtonStyled
from wse.features.shared.ui.heading import Heading
from wse.utils.i18n import _


class HomeView(ColumnFlexBox, Source):
    """Represents the home screen."""

    def __init__(self) -> None:
        """Construct the view."""
        super().__init__()
        Source.__init__(self)
        self._create_widgets()
        self._add_widgets_to_view()

    def _create_widgets(self) -> None:
        self.heading = Heading(_('Home'))
        self.flex_box = ColumnFlexBox()
        self.exercise_button = ButtonStyled(_('Exercises'))
        self.exercise_button.on_press = self._on_exercises_click

    def _add_widgets_to_view(self) -> None:
        self.add(
            self.heading,
            self.flex_box,
            self.exercise_button,
        )

    ####################################################################
    # Button handlers

    def _on_exercises_click(self, _: toga.Widget) -> None:
        self.notify('handel_exercises')
