"""Configures logging settings for the application."""

import json
import logging.config
from datetime import datetime
from pathlib import Path

from wse.config.config import PROJECT_PATH

CONFIG_PATH: Path = PROJECT_PATH / 'src' / 'wse' / 'config' / 'logging.json'
LOG_DIR: Path = PROJECT_PATH / 'logs_src'

FALLBACK_LOG_PATH: Path = LOG_DIR / 'fallback.log'
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


class AppLogging:
    """Application logging system.

    Configures log handlers, sets output paths with timestamps,
    and optionally cleans up old log files based on retention policy.
    """

    _log_dir: Path = LOG_DIR

    def __new__(cls, *args, **kwargs):
        """Ensure log directory exists and return instance."""
        cls._create_log_dir()
        instance = super().__new__(cls)
        return instance

    def __init__(self) -> None:
        """Construct the logging."""
        # Load logging configuration
        self._config_path = Path(CONFIG_PATH)
        self._config = self._load_base_config_safe()

        if self._config:
            # Get logging settings
            settings = self._config['logging_settings']

            # Setting up log storage
            self._enable_file_limit = settings['enable_file_limit']
            self._max_files = settings['max_log_files']

            # Loggers for saving to file
            self._handlers_to_file = settings['handlers_to_file']

            # The log file name starts with a timestamp.
            self._timestamp = datetime.now().strftime(settings['timestamp'])

            # Set up core logging
            self._setup_core_logging()

    @property
    def log_dir(self) -> Path:
        """Path to the log directory (class variable, reade-only)."""
        return self.__class__._log_dir

    def _load_base_config_safe(self) -> dict:
        try:
            config_content = self._config_path.read_text(encoding='utf-8')
            return json.loads(config_content)
        except Exception as e:
            # Using a backup configuration
            self._setup_fallback_logging(e)
            return {}

    def _setup_core_logging(self) -> None:
        self._load_base_config()
        self._create_timestamp_name()
        logging.config.dictConfig(self._config)
        self._check_logs_limit()

    @classmethod
    def _create_log_dir(cls) -> None:
        cls._log_dir.mkdir(parents=True, exist_ok=True)

    def _load_base_config(self) -> dict:
        config_content = self._config_path.read_text(encoding='utf-8')
        return json.loads(config_content)

    def _create_timestamp_name(self) -> None:
        """Create timestamp log file name."""
        for handler in self._handlers_to_file:
            filename = self._config['handlers'][handler]['filename']

            # The log file name has a timestamp.
            self._config['handlers'][handler]['filename'] = str(
                self.log_dir / f'{self._timestamp}_{filename}',
            )

    def _check_logs_limit(self) -> None:
        if self._enable_file_limit:
            self._cleanup_logs()

    def _cleanup_logs(self) -> None:
        logger = logging.getLogger(__name__)

        for logger_name in self._handlers_to_file:
            parts = logger_name.split('_', 1)
            if len(parts) != 2:
                continue  # Skipping invalid logger names.

            prefix = parts[1]
            pattern = f'*_{prefix}.log'
            log_files = list(self._log_dir.glob(pattern))
            log_files.sort()  # Sort ascending (oldest files first).

            if len(log_files) > self._max_files:
                num_files_to_remove = len(log_files) - self._max_files
                files_to_remove = log_files[:num_files_to_remove]

                for file_path in files_to_remove:
                    try:
                        file_path.unlink()
                        logger.info(f'Deleted old log file: {file_path}')
                    except Exception as e:
                        logger.exception(f'Failed to delete {file_path}: {e}')

    @classmethod
    def _setup_fallback_logging(cls, error: Exception) -> None:
        """Set up fallback logging for configuration errors."""
        logging.config.dictConfig(FALLBACK_CONFIG)

        # Log the configuration error itself
        logger = logging.getLogger(__name__)
        logger.error(
            'Failed to load main logging config. Using fallback. Error: %s',
            str(error),
            exc_info=True,
        )


def setup_logging() -> AppLogging:
    """Set up logging."""
    return AppLogging()
