"""Defines navigation page route enums."""

from wse.core.base.enums import BaseEnum


class NavID(BaseEnum):
    """Navigation route enums."""

    # Utility ID
    BACK = 'move to previous page'

    # Auth
    LOGIN = 'Login page'
    LOGOUT = 'Logout page'

    # Main app
    HOME = 'Home page'

    # Math app
    INDEX_MATH = 'Main math page'
    SIMPLE_CALC = 'Simple math calculation page'
