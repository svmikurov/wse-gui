"""Defines unique button names."""

from enum import Enum, unique

from wse.core.i18n import _


class BaseButtonName(str, Enum):
    """Base class for creating button enumerations."""

    def __str__(self) -> str:
        """Return button text."""
        return self.value


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
    NOT_SET = _('Not set')

    # Foreign
    FOREIGN = _('Foreign')
    FOREIGN_TASKS = _('Foreign tasks')
    FOREIGN_TESTS = _('Foreign tests')
    FOREIGN_PARAMS = _('Foreign params')
    FOREIGN_EXERCISE = _('Foreign exercise')
    FOREIGN_CREATE = _('Foreign create')
    FOREIGN_UPDATE = _('Foreign update')

    # Glossary
    GLOSSARY = _('Glossary')
    MATHEM = _('Mathematics')
    EXERCISES = _('Exercises')
