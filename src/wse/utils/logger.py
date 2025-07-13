"""Defines logging system initialization."""

import json
import logging.config
from pathlib import Path
from typing import Any

from wse.config.settings import CONFIGS_PATH, RESOURCES_PATH

LOGGER_NAME = 'wse'
LOGGER_CONFIG_PATH = CONFIGS_PATH / 'logging.json'
LOG_FILE_PATH = RESOURCES_PATH / 'logs' / 'wse.log'
# Check and create a directory if it doesn't exist
LOG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)


def fallback_logger(
    log_file: str | Path = LOG_FILE_PATH,
    console_level: int = logging.INFO,
    file_level: int = logging.DEBUG,
) -> None:
    """Set up logging with output to the console and file."""
    log_format = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    # Core logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_formatter = logging.Formatter(log_format, datefmt=date_format)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(file_level)
    file_formatter = logging.Formatter(log_format, datefmt=date_format)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)


def setup_logger() -> None:
    """Initialize application logging system."""
    try:
        with open(LOGGER_CONFIG_PATH, 'r') as f:
            logging_config: dict[str, Any] = json.load(f)

            # Change the path to the log file
            logging_config['handlers']['file']['filename'] = str(LOG_FILE_PATH)

            # Applying the configuration
            logging.config.dictConfig(logging_config)
            logger = logging.getLogger(LOGGER_NAME)

            # Success configurate message
            logger.info(
                'Logging is set up (console + "%s" file)', LOG_FILE_PATH
            )

    except Exception as e:
        fallback_logger()
        logger = logging.getLogger()
        logger.error('Error loading logger configuration:\n%s', e)
        logger.info(
            'Set up fallback logger (console + "%s" file)', LOG_FILE_PATH
        )
