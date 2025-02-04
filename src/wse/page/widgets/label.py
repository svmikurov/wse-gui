"""General label widget."""

import toga
from travertino.constants import CENTER

from wse.constants import TITLE_LABEL_FONT_SIZE, TITLE_LABEL_PADDING


class LabelParam(toga.Label):
    """Styled label of exercise parameters."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the style of label."""
        super().__init__(*args, **kwargs)
        self.style.padding = (7, 0, 7, 2)


class TitleLabel(toga.Label):
    """General title label."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the label."""
        super().__init__(*args, **kwargs)
        self.style.text_align = CENTER
        self.style.font_size = TITLE_LABEL_FONT_SIZE
        self.style.padding = TITLE_LABEL_PADDING
