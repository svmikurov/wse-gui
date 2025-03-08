"""Defines the exercises screen view."""

from wse.features.shared.ui.box import ColumnFlexBox
from wse.features.shared.ui.button import ButtonStyled
from wse.features.shared.ui.heading import Heading
from wse.utils.i18n import _


class ExerciseView(ColumnFlexBox):
    """Represents the exercises screen."""

    def __init__(self) -> None:
        """Construct the view."""
        super().__init__()
        self._create_widgets()
        self._add_widgets_to_view()

    def _create_widgets(self) -> None:
        self.heading = Heading(_('Exercises'))
        self.back_button = ButtonStyled(_('Back'))

    def _add_widgets_to_view(self) -> None:
        self.add(
            self.heading,
            self.back_button,
        )
