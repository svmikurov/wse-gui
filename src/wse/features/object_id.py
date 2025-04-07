"""Application object test ID enumeration."""

from enum import Enum, unique


@unique
class ObjectID(str, Enum):
    """Application object ID enumeration."""

    HOME = 'Home view'
    FOREIGN = 'Foreign home view'
    FOREIGN_PARAMS = 'Foreign params view'
    FOREIGN_TASKS = 'Foreign tasks view'
    FOREIGN_TEST = 'Foreign test view'
