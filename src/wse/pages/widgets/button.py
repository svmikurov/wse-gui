"""General app buttons."""

import toga

from wse.constants import BUTTON_HEIGHT, FONT_SIZE_APP


class BtnApp(toga.Button):
    """General button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = BUTTON_HEIGHT
        self.style.font_size = FONT_SIZE_APP


class SmBtn(toga.Button):
    """Small button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = 45


class AnswerBtn(toga.Button):
    """User answer button."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the button."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.style.height = 100
        self.style.font_size = 9
