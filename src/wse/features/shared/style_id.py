"""Defines widget stile ID enumeration."""

from enum import Enum, unique


@unique
class StyleID(Enum):
    """Widget stile ID enumeration."""

    def __init__(self, style_config: dict):
        super().__init__()
        self.style_config = style_config

    LABEL = 'Label'
    LABEL_RED = 'Label model'
    LABEL_GREEN = 'Label input'
