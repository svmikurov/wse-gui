"""Defines unique button names."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class NavigationID(BaseEnum):
    """Application navigation ID enumeration."""

    # Authentication
    ACCOUNT = 'Account'
    LOGIN = 'Login'
    LOGOUT = 'Logout'

    # Main
    HOME = 'Home'
    BACK = 'Back'
    NOT_SET = 'Not set'

    # -=== Education ===-
    EDUCATION = 'Education'

    # Foreign
    FOREIGN = 'Foreign'
    FOREIGN_TASKS = 'Foreign tasks'
    FOREIGN_TESTS = 'Foreign tests'
    FOREIGN_PARAMS = 'Foreign params'
    FOREIGN_EXERCISE = 'Foreign exercise'
    FOREIGN_CREATE = 'Foreign create'
    FOREIGN_UPDATE = 'Foreign update'

    # Glossary
    GLOSSARY = 'Glossary'

    # Mathematical
    MATHEMATICAL = 'Mathematical'
    MULTIPLICATION = 'Multiplication'

    # Exercises
    EXERCISES = 'Exercises'

    # -=== Figaro ===-
    FIGARO = 'Figaro'
    SWARM = 'Swarm'

    # -=== Examples ===-
    EXAMPLES = 'Examples'
