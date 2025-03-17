"""Main logging configuration handler."""

import json
import logging.config
from datetime import datetime
from pathlib import Path

from .config import CONFIG_PATH, LOG_DIR, PROJECT_PATH


class AppLogging:
    """Core application logging system."""

    _log_dir: Path = LOG_DIR

    def __init__(self) -> None:
        """Construct the logging system."""
        self._create_log_directory()
        self._config_path = CONFIG_PATH
        self._config = self._load_config()
        self._apply_config()

    @classmethod
    def _create_log_directory(cls) -> None:
        """Гарантированное создание директории для логов."""
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        logging.getLogger(__name__).debug(f'Log directory: {LOG_DIR}')

    def _load_config(self) -> dict:
        """Load JSON logging configuration."""
        try:
            config_content = self._config_path.read_text(encoding='utf-8')
            return json.loads(config_content)
        except Exception as e:
            raise RuntimeError('Failed to load main config') from e

    def _apply_config(self) -> None:
        """Apply logging configuration."""
        self._prepare_log_files()
        logging.config.dictConfig(self._config)
        self._cleanup_old_logs()

    def _prepare_log_files(self) -> None:
        """Add timestamp to log filenames."""
        settings = self._config['logging_settings']
        timestamp = datetime.now().strftime(settings['timestamp'])

        for handler in settings['handlers_to_file']:
            filename = self._config['handlers'][handler]['filename']
            self._config['handlers'][handler]['filename'] = str(
                self._log_dir / f'{timestamp}_{filename}'
            )

    def _cleanup_old_logs(self) -> None:
        """Enforce log retention policy."""
        settings = self._config['logging_settings']
        if not settings['enable_file_limit']:
            return

        logger = logging.getLogger(__name__)
        for handler in settings['handlers_to_file']:
            prefix = handler.split('_', 1)[1]
            log_files = sorted(self._log_dir.glob(f'*_{prefix}.log'))

            if len(log_files) > settings['max_log_files']:
                for file in log_files[: -settings['max_log_files']]:
                    try:
                        rel_path = file.relative_to(PROJECT_PATH)
                        file.unlink()
                        logger.info(f'Deleted old log: {rel_path}')
                    except ValueError:
                        logger.info(f'Deleted old log: {file}')
                    except Exception as e:
                        logger.error(f'Error deleting {file}: {e}')
