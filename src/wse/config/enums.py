"""Defines layout style enumerations."""

from wse.core.base.enums import BaseEnum

# Language localization


class Language(BaseEnum):
    """Localization language enumeration."""

    EN = 'en'
    RU = 'ru'


class LocaleDomain(BaseEnum):
    """Localization domain enumeration."""

    CORE = 'core'
    NAV = 'nav'
    LABEL = 'label'
    EXERCISE = 'exercise'


# Layout


class TaskIO(BaseEnum):
    """Task I/O widget enumeration."""

    INTEGER = 'integer'
    TEXT = 'text'


# UI styles


class LayoutTheme(BaseEnum):
    """Layout color theme enumeration."""

    DEFAULT = 'theme_default.json'
    DEVELOP = 'theme_develop.json'
    GREEN = 'theme_green.json'


class LayoutStyle(BaseEnum):
    """Layout style enumeration."""

    DEFAULT = 'style_default.json'
    DEVELOP = 'style_develop.json'
