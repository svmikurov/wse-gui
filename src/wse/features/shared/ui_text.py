"""Text styled widgets."""

import toga
from toga.constants import CENTER

from wse.features.settings import TITLE_LABEL_FONT_SIZE, TITLE_LABEL_PADDING
from wse.features.shared.observer import ValueListenerMixin


class TitleLabel(toga.Label):
    """General title label."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the label."""
        super().__init__(*args, **kwargs)
        self.style.text_align = CENTER
        self.style.font_size = TITLE_LABEL_FONT_SIZE
        self.style.padding = TITLE_LABEL_PADDING


class LabelParam(toga.Label):
    """Styled label of parameters."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the style of label."""
        super().__init__(*args, **kwargs)
        self.style.padding = (7, 0, 7, 2)


class MultilineInfoPanel(ValueListenerMixin, toga.MultilineTextInput):
    """Text panel for info display."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        kwargs.setdefault('value', '')
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.readonly = True
