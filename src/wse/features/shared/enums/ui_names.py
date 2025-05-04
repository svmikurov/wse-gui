"""Defines UI name enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class UIName(BaseEnum):
    """UI name enumeration."""

    ANSWER_DISPLAY = 'answer_display'
    INFO_DISPLAY = 'info_display'
    QUESTION_DISPLAY = 'question_display'
