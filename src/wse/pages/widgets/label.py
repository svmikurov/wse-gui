"""General label widget."""

import toga
from toga.style import Pack
from travertino.constants import CENTER

from wse.constants import TITLE_LABEL_FONT_SIZE, TITLE_LABEL_PADDING


class LabelParam(toga.Label):
    """Styled label of parameter."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the style of label."""
        super().__init__(*args, **kwargs)
        self.style.padding = (7, 0, 7, 2)


class TitleLabel(toga.Label):
    """General title label.

    Defines a common style for derived label widgets.
    """

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the label."""
        style = Pack(
            # flex=1,
            text_align=CENTER,
            font_size=TITLE_LABEL_FONT_SIZE,
            padding=TITLE_LABEL_PADDING,
        )
        kwargs['style'] = kwargs.pop('style', style)
        super().__init__(*args, **kwargs)
