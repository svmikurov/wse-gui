"""Defines the exercises screen view."""

import toga
from toga.sources import Source

from wse.features.shared.ui.box import ColumnFlexBox
from wse.features.shared.ui.button import ButtonStyled
from wse.features.shared.ui.heading import Heading
from wse.features.shared.ui.text import MultilineInfoPanel
from wse.utils.i18n import _


class ExercisesView(ColumnFlexBox, Source):
    """Represents the main exercises screen."""

    def __init__(self) -> None:
        """Construct the view."""
        super().__init__()
        Source.__init__(self)
        self._create_widgets()
        self._add_widgets_to_view()

    def _create_widgets(self) -> None:
        self.heading = Heading(_('Exercises'))
        self.info_panel = MultilineInfoPanel()
        self.back_button = ButtonStyled(
            _('Back'), on_press=self._on_back_click
        )

    def _add_widgets_to_view(self) -> None:
        self.add(
            self.heading,
            self.info_panel,
            self.back_button,
        )

    ####################################################################
    # Widget handlers

    def _on_back_click(self, _: toga.Widget) -> None:
        self.notify('back')
