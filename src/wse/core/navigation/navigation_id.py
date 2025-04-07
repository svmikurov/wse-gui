"""Defines unique button names."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class NavigationID(BaseEnum):
    """Application navigation ID enumeration."""

    # Authentication
    LOGIN = 'Login'
    LOGOUT = 'Logout'

    # Actions
    CANCEL = 'Cancel'
    CONFIRM = 'Confirm'

    # Main
    HOME = 'Home'
    BACK = 'Back'
    NOT_SET = 'Not set'

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
    MATHEM = 'Mathematics'
    EXERCISES = 'Exercises'
