"""Logging system initialization."""

import logging
from pathlib import Path

from wse.config.config import PROJECT_PATH
from wse.core.logger.custom import CustomLogging
from wse.core.logger.fallback import setup_fallback_logger

CONFIG_PATH: Path = PROJECT_PATH / 'src' / 'wse' / 'config' / 'logging.json'
LOG_DIR: Path = PROJECT_PATH / 'logs_src'
FALLBACK_LOG_PATH: Path = LOG_DIR / 'fallback.log'

logger = logging.getLogger(__name__)


def setup_logging() -> None:
    """Initialize application logging system."""
    try:
        CustomLogging(config_path=CONFIG_PATH, log_dir=LOG_DIR)
    except Exception as e:
        setup_fallback_logger(name='root', log_file=FALLBACK_LOG_PATH)
        logger.exception(
            'Error setup from logging config. Using backup log. Error: %s',
            str(e),
        )
