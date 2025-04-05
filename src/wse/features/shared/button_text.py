"""Defines unique button names."""

from enum import unique

from wse.core.i18n import _
from wse.features.shared.base import BaseButtonName


@unique
class ButtonText(BaseButtonName):
    """Application button name enumeration."""

    # Authentication
    LOGIN = _('Login')
    LOGOUT = _('Logout')

    # Actions
    CANCEL = _('Cancel')
    CONFIRM = _('Confirm')

    # -= Navigation =-
    # Main
    HOME = _('Home')
    BACK = _('Back')

    # Foreign
    FOREIGN = _('Foreign')
    FOREIGN_TASKS = _('Foreign tasks')
    FOREIGN_PARAMS = _('Foreign params')
    FOREIGN_CREATE = _('Foreign create')

    # Glossary
    GLOSSARY = _('Glossary')
    MATHEM = _('Mathematics')
    EXERCISES = _('Exercises')
