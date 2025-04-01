"""Text styled widgets."""

import toga
from toga.constants import CENTER

from wse.features.settings import TITLE_LABEL_FONT_SIZE, TITLE_LABEL_PADDING


class TitleLabel(toga.Label):
    """General title label."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the label."""
        super().__init__(*args, **kwargs)
        self.style.text_align = CENTER
        self.style.font_size = TITLE_LABEL_FONT_SIZE
        self.style.padding = TITLE_LABEL_PADDING
