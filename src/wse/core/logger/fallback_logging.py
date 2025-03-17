"""Fallback logging configuration."""

import logging.config

from .config import FALLBACK_LOG_PATH, LOG_DIR


class FallbackLogging:
    """Emergency logging system for configuration errors."""

    def __init__(self, error: Exception) -> None:
        """Construct the fallback logging system."""
        self._setup_logging(error)

    @staticmethod
    def _setup_logging(error: Exception) -> None:
        """Activate fallback logging."""
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        logging.config.dictConfig(FALLBACK_CONFIG)

        logger = logging.getLogger(__name__)
        logger.error(
            'Failed to load main logging config. Using fallback. Error: %s',
            str(error),
            exc_info=True,
        )


FALLBACK_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
        },
        'fallback_file': {
            'class': 'logging.FileHandler',
            'filename': str(FALLBACK_LOG_PATH),
            'mode': 'a',
            'level': 'DEBUG',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'fallback_file'],
        'propagate': False,
    },
}
