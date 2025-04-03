"""Defines unique button names."""

from enum import unique

from wse.core.i18n import _
from wse.features.shared.base import BaseButtonName


@unique
class ButtonName(BaseButtonName):
    """Application button name enumeration."""

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
