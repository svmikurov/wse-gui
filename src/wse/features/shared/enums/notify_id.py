"""Subject notification event enumeration for the application."""

from enum import auto, unique

from wse.core.base import BaseEnum


@unique
class NotifyID(BaseEnum):
    """Subject notification types with clear categories."""

    # Data (model)
    DATA_EXERCISE_LIST_UPDATED = auto()  # The list of exercises has changed
    DATA_DEFAULT_EXERCISE_SET = auto()  # Default exercise set

    # Exercises
    DATA_TASK_CREATED = auto()
    DATA_ANSWER_CHECKED = auto()

    # UI Actions (Signals for View)
    UI_FIELD_VALUE_UPDATED = auto()  # Field value changed (general)
    UI_FIELD_CLEARED = auto()  # Field cleared
    UI_PAGE_CLEARED = auto()  # Page reset

    # System Events
    SYSTEM_ERROR = auto()  # Error (for logging)
