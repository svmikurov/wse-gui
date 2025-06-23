"""Defines layout style enumerations."""

from wse.core.base.enums import BaseEnum


class Languages(BaseEnum):
    """Localisation langauge enumerations."""

    EN = 'en'
    RU = 'ru'


class ColorStyles(BaseEnum):
    """Layout color enumerations."""

    DEFAULT = 'default'
    BLACK = 'black'


class LayoutStyles(BaseEnum):
    """Layout style enumerations."""

    DEFAULT = 'layout_default_style.json'
