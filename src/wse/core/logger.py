"""Configures logging settings for the application."""

import glob
import json
import logging.config
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from wse.config.config import PROJECT_PATH

LOGGING_CONFIG_PATH = PROJECT_PATH / 'src/wse/config/logging.json'
LOG_DIR = PROJECT_PATH / 'logs_src'
MAX_LOG_FILES = 3


def setup_logging(
    enable_file_limit: bool = True, max_files: Optional[int] = None
) -> None:
    """Initialize the logging system for the application.

    Configures log handlers, sets output paths with timestamps,
    and optionally cleans up old log files based on retention policy.

    :param enable_file_limit: Enable log file rotation and deletion.
    :param max_files: Maximum number of log files to retain. If None,
        uses MAX_LOG_FILES value.
    """
    log_dir = Path(LOG_DIR)
    log_dir.mkdir(parents=True, exist_ok=True)

    config = load_base_config()
    timestamp = datetime.now().strftime('%Y_%m_%d-%H_%M_%S')

    # Modify log paths
    config['handlers']['file_all']['filename'] = str(
        log_dir / f'{timestamp}_all.log',
    )
    config['handlers']['file_features']['filename'] = str(
        log_dir / f'{timestamp}_features.log',
    )

    logging.config.dictConfig(config)

    # Clean up logs only if the limit is enabled
    if enable_file_limit:
        cleanup_old_logs(max_files or MAX_LOG_FILES)


def load_base_config() -> dict:
    """Load the base logging configuration from the JSON file.

    :return: Dictionary with logging configuration
    """
    config_path = Path(LOGGING_CONFIG_PATH)
    config_content = config_path.read_text(encoding='utf-8')
    return json.loads(config_content)


def cleanup_old_logs(max_files: int) -> None:
    """Delete old log files to maintain the specified maximum count.

    Processes both 'all' and 'features' log files separately. Removes
    oldest files first when exceeding the limit.

    :param max_files: Maximum number of log files to retain per type
    """
    patterns = [f'{LOG_DIR}/*_all.log', f'{LOG_DIR}/*_features.log']

    for pattern in patterns:
        files = sorted(glob.glob(pattern), key=os.path.getctime, reverse=True)
        delete_count = len(files) - max_files

        if delete_count > 0:
            logger = logging.getLogger('logger_config')
            logger.debug(
                f'Cleaning logs: {pattern}, keeping {max_files} files'
            )

            for old_file in files[max_files:]:
                try:
                    os.remove(old_file)
                except Exception as e:
                    logging.error(f'Failed to delete {old_file}: {str(e)}')
