"""Defines UI name enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class UIName(BaseEnum):
    """UI name enumeration."""

    QUESTION_DISPLAY = 'question_display'
    ANSWER_DISPLAY = 'answer_display'
