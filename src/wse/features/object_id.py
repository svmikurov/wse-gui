"""Application object test ID enumeration."""

from enum import Enum, unique


@unique
class ObjectID(str, Enum):
    """Application object test ID enumeration."""

    HOME_VIEW = 'Home view'
    FOREIGN_VIEW = 'Foreign home view'
    FOREIGN_TASKS = 'Foreign tasks view'
    FOREIGN_TEST = 'Foreign test view'
