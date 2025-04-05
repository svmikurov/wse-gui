"""Application object test ID enumeration."""

from enum import Enum, unique


@unique
class ObjectTestID(str, Enum):
    """Application object test ID enumeration."""

    HOME_VIEW = 'Home view'
    FOREIGN_VIEW = 'Foreign home view'
