"""Defines navigation page route enums."""

from wse.core.base.enums import BaseEnum


class NavID(BaseEnum):
    """Navigation route enums."""

    # Utility ID
    BACK = 'Move to previous page'

    # Auth
    LOGIN = 'Login page'
    LOGOUT = 'Logout page'

    # Main app
    HOME = 'Home page'
    ASSIGNED = 'Assigned exercises page'
    EXERCISE = 'Exercise completion page'

    # Math app
    INDEX_MATH = 'Main math page'
    SIMPLE_CALC = 'Simple math calculation page'

    # UI route
    CALCULATION = 'Calculation'
    MATH_INDEX = 'Main math page'
