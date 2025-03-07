"""Defines user interface settings and configurations."""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class UIStyle:
    """Stores style settings for user interface widgets."""

    # Heading style settings
    HEADING_FONT_SIZE: int = 18
    HEADING_HEIGHT: int = 35
    HEADING_PADDING: Tuple[int, int, int, int] = (5, 0, 10, 0)

    # Button style settings
    BUTTON_FONT_SIZE: int = 20
    BUTTON_HEIGHT: int = 70
    BUTTON_PADDING: Tuple[int, int, int, int] = (10, 25, 10, 25)
