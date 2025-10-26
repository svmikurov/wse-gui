"""Defines navigation screen route enums."""

from wse.core.base.enums import BaseEnum


class NavID(BaseEnum):
    """Navigation route enums."""

    # Utility ID
    BACK = 'Move to previous screen'

    # Main
    HOME = 'Home screen'
    ASSIGNED = 'Assigned exercises screen'
    EXERCISE = 'Exercise completion screen'

    # Auth
    LOGIN = 'Login screen'
    LOGOUT = 'Logout'
    ACCOUNT = 'Account screen'

    # Math
    MATH = 'Main math screen'
    CALCULATION = 'Calculation screen'

    # Glossary
    GLOSSARY = 'Glossary index screen'
    TERMS = 'Terms screen'
    TERMS_STUDY = 'Study terms'

    # Foreign
    FOREIGN = 'Foreign index screen'
    FOREIGN_PARAMS = 'Word study params screen'
    FOREIGN_STUDY = 'Word study screen'

    @property
    def name(self) -> str:
        """Get text representation of navigation route."""
        return self.value
