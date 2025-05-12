"""Application object test ID enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class ObjectID(BaseEnum):
    """Application object ID enumeration."""

    ACCOUNT = 'Account'
    EDUCATION = 'Education view'
    EXAMPLES = 'Examples view'
    FIGARO = 'Figaro view'
    FOREIGN = 'Foreign view'
    FOREIGN_PARAMS = 'Foreign params view'
    FOREIGN_TASKS = 'Foreign tasks view'
    FOREIGN_TEST = 'Foreign test view'
    HOME = 'Home view'
    LOGIN = 'Login'
    MATHEMATICAL = 'Mathematical view'
    MATH_EXERCISE_SELECTION = 'Mathematical exercise selection'
    MULTIPLICATION = 'Multiplication view'
    PRACTICE = 'Practice view'
    SWARM = 'Swarm view'
