"""Application exceptions."""


class NavigateError(Exception):
    """Raised when navigation between pages fails."""


class AuthError(Exception):
    """Raised when an error occurs in performing an authentication."""


class ExerciseError(Exception):
    """Raised when an error occurs in performing an exercise."""


class ExerciseAttributeError(ExerciseError):
    """Raised when an error occurs in performing an exercise."""


class StorageError(Exception):
    """Raised when an error occurs in storage service."""
