"""Logging system initialization."""

import json
import logging.config
from pathlib import Path

PROJECT_PATH = Path(__file__).parents[4]
CONFIG_PATH = PROJECT_PATH / 'src' / 'wse' / 'config' / 'logging_config.json'
LOG_DIR: Path = PROJECT_PATH / 'logs_wse'
LOGGER_NAME = 'wse'


def setup_logging() -> None:
    """Initialize application logging system."""
    try:
        with open(CONFIG_PATH, 'r') as f:
            config: dict = json.load(f)

        # Logs path
        log_file_path = PROJECT_PATH / 'logs_wse' / 'wse.log'
        config['handlers']['file']['filename'] = str(log_file_path)

        logging.config.dictConfig(config)
        logger = logging.getLogger(LOGGER_NAME)

        # Success configurate message
        logger.info('The logger has been successfully configured.')

    except Exception as e:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().error('Error loading logger configuration: %s', e)
