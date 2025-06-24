"""Defines layout style enumerations."""

from wse.core.base.enums import BaseEnum

# Langauge localization


class Language(BaseEnum):
    """Localisation langauge enumerations."""

    EN = 'en'
    RU = 'ru'


class LocaleDomain(BaseEnum):
    """Localization domain enumeration."""

    NAV = 'nav'
    LABEL = 'label'


# UI styles


class LayoutTheme(BaseEnum):
    """Layout color theme enumerations."""

    DEFAULT = 'theme_default.json'
    DEVELOP = 'theme_develop.json'
    GREEN = 'theme_green.json'


class LayoutStyle(BaseEnum):
    """Layout style enumerations."""

    DEFAULT = 'style_default.json'
    DEVELOP = 'style_develop.json'
