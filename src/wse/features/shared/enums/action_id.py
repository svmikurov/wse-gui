"""Defines actions ID enumeration."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class ActionID(BaseEnum):
    """Action ID enumeration."""

    CHECK_ANSWER = 'Check answer'
