"""Defines widget stile ID enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class StyleID(BaseEnum):
    """Widget stile ID enumeration."""

    KEYPAD_BUTTON = 'Keypad button'

    LABEL = 'Label'
    LABEL_RED = 'Label model'
    LABEL_GREEN = 'Label input'
