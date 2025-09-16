"""Defines navigation page route enums."""

from wse.core.base.enums import BaseEnum


class NavID(BaseEnum):
    """Navigation route enums."""

    # Utility ID
    BACK = 'Move to previous page'

    # Auth
    LOGIN = 'Login page'
    LOGOUT = 'Logout page'
    ACCOUNT = 'Account screen'

    # Main
    HOME = 'Home page'
    ASSIGNED = 'Assigned exercises page'
    EXERCISE = 'Exercise completion page'

    # Math
    MATH = 'Main math page'
    CALCULATION = 'Calculation'

    # Glossary
    GLOSSARY = 'Glossary index screen'
    TERMS = 'Terms screen'
