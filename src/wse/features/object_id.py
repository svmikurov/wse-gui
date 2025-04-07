"""Application object test ID enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class ObjectID(BaseEnum):
    """Application object ID enumeration."""

    HOME = 'Home view'
    FOREIGN = 'Foreign home view'
    FOREIGN_PARAMS = 'Foreign params view'
    FOREIGN_TASKS = 'Foreign tasks view'
    FOREIGN_TEST = 'Foreign test view'
