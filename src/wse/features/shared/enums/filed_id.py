"""Defines UI name enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class FieldID(BaseEnum):
    """Model field name enumeration."""

    EXERCISE_SELECTION = 'Exercise selection'
    QUESTION_TEXT = 'Display info'
    RESULT_STATUS = 'Display question'
    USER_INPUT = 'Display answer'
