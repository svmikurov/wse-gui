"""Application object test ID enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class ObjectID(BaseEnum):
    """Application object ID enumeration."""

    HOME = 'Home view'
    ACCOUNT = 'Account'
    LOGIN = 'Login'
    FOREIGN = 'Foreign view'
    FOREIGN_PARAMS = 'Foreign params view'
    FOREIGN_TASKS = 'Foreign tasks view'
    FOREIGN_TEST = 'Foreign test view'
    PRACTICE = 'Practice view'
    SWARM = 'Swarm view'
    FIGARO = 'Figaro view'
    EDUCATION = 'Education view'
    MATHEMATICAL = 'Mathematical view'
    MULTIPLICATION = 'Multiplication view'
