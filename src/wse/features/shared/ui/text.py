import toga

from wse.features.ui_config import UIStyle


class MultilineInfoPanel(toga.MultilineTextInput):
    """Text panel for info display."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)
        self.readonly = True
        self.style.font_size = UIStyle.INFO_FONT_SIZE
        self.style.padding = UIStyle.INFO_PANEL_PADDING
