"""Defines task answer checking result."""

import logging

logger = logging.getLogger(__name__)


class CheckResult:
    """Task answer checking result."""

    def __init__(self) -> None:
        """Construct the check result."""
        self._is_correct = None

    @property
    def is_correct(self) -> bool:
        """Return is correct user answer (`bool`)."""
        if self._is_correct is not None:
            return self._is_correct
        else:
            logger.info(
                'The answer result check was requested before the check.'
            )
            return False

    @is_correct.setter
    def is_correct(self, value: bool) -> None:
        self._is_correct = value

    def __str__(self) -> str:
        """The string representation of check result."""
        return str(self.is_correct)