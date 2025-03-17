"""Logging system initialization."""

from typing import Union

from .fallback_logging import FallbackLogging
from .main_logging import AppLogging


def setup_logging() -> Union[AppLogging, FallbackLogging]:
    """Initialize application logging system."""
    try:
        return AppLogging()
    except Exception as e:
        return FallbackLogging(e)
