"""Application object test ID enumeration."""

from enum import Enum, unique


@unique
class ObjectID(str, Enum):
    """Application object test ID enumeration."""

    HOME = 'Home view'
    FOREIGN = 'Foreign home view'
    FOREIGN_TASKS = 'Foreign tasks view'
    FOREIGN_TEST = 'Foreign test view'
