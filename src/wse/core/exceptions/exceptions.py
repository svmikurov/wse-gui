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


class ViewCallError(Exception):
    """Raised when an error occurs in injection."""

    def __init__(self) -> None:
        """Construct the exception."""
        help_message = (
            'Check whether the injected object was associated with an '
            'abstract base class. An exception was thrown indicating '
            'that the abstract methods of an injected object annotated '
            'as abstract were not implemented.'
        )
        super().__init__(help_message)
