"""Defines action ID."""

from enum import unique

from wse.core.base import BaseEnum


@unique
class ActionID(BaseEnum):
    """Action ID."""

    CANCEL = 'Cancel'
    CONFIRM = 'Confirm'
    SUBMIT = 'Submit'
