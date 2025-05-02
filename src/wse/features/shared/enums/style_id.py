"""Defines widget stile ID enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class StyleID(BaseEnum):
    """Widget stile ID enumeration."""

    TITLE = 'Title'
    DEFAULT_LABEL = 'Default label'
    DEFAULT_BUTTON = 'Default button'
    KEYPAD_BUTTON = 'Keypad button'
    LINE_DISPLAY = 'Single line display'
