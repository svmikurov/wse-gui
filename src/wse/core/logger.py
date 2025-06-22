"""Defines logging system initialization."""

import json
import logging.config
from typing import Any

from wse.config.settings import CONFIGS_PATH, PROJECT_PATH

LOGGER_CONFIG_PATH = CONFIGS_PATH / 'logging.json'
LOG_FILE_PATH = PROJECT_PATH.parents[2] / 'logs_wse' / 'wse.log'
LOGGER_NAME = 'wse'


def setup_logger() -> None:
    """Initialize application logging system."""
    try:
        with open(LOGGER_CONFIG_PATH, 'r') as f:
            logging_config: dict[str, Any] = json.load(f)

        logging.config.dictConfig(logging_config)
        logger = logging.getLogger(LOGGER_NAME)

        # Log files path
        logging_config['handlers']['file']['filename'] = str(LOG_FILE_PATH)

        # Success configurate message
        logger.info('The logger has been successfully configured.')

    except Exception as e:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().error('Error loading logger configuration: %s', e)
