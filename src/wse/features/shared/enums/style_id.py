"""Defines widget stile ID enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class StyleID(BaseEnum):
    """Widget stile ID enumeration."""

    DEFAULT_BUTTON = 'Default button'
    DEFAULT_LABEL = 'Default label'
    KEYPAD_BUTTON = 'Keypad button'
    LINE_DISPLAY = 'Line display'
    NO_STYLE = 'No style'
    RESULT_INFO_DISPLAY = 'Result info display'
    TITLE = 'Title'
