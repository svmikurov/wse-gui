"""Defines unique button names."""

from enum import Enum, unique

from wse.core.i18n import _


@unique
class ButtonName(str, Enum):
    """Application button names."""

    # Authentication
    LOGIN = _('Login')
    LOGOUT = _('Logout')

    # Actions
    CANCEL = _('Cancel')
    CONFIRM = _('Confirm')

    # Navigation
    HOME = _('Home')
    FOREIGN_HOME = _('Foreign')
    GLOSSARY_HOME = _('Glossary')
    MATHEM_HOME = _('Mathematics')
    EXERCISES_HOME = _('Exercises')
