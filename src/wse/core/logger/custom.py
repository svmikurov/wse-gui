"""Main logging configuration handler."""

import json
import logging
import logging.config
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


class CustomLogging:
    """Custom application logging system."""

    def __init__(self, config_path: Path, log_dir: Path) -> None:
        """Initialize logging system with configuration."""
        self.logger = logging.getLogger(__name__)
        self._config_path = config_path
        self._log_dir = log_dir
        self._config = self._load_json_config()
        self._settings = self._config['logging_settings']

        self._create_log_directory()
        self._apply_config()

    def _create_log_directory(self) -> None:
        """Ensure log directory exists."""
        self._log_dir.mkdir(parents=True, exist_ok=True)
        self.logger.debug('Log directory: %s', self._log_dir)

    def _load_json_config(self) -> Dict[str, Any]:
        """Load and validate json logging configuration."""
        if not self._config_path.exists():
            raise FileNotFoundError(
                f'Config file {self._config_path} not found'
            )

        try:
            config_content = self._config_path.read_text(encoding='utf-8')
            return json.loads(config_content)
        except json.JSONDecodeError as e:
            raise RuntimeError(f'Invalid JSON in config: {e}') from e
        except Exception as e:
            raise RuntimeError(f'Error loading config: {e}') from e

    def _apply_config(self) -> None:
        """Apply logging configuration with dynamic filenames."""
        self._prepare_log_files()
        logging.config.dictConfig(self._config)
        self._cleanup_old_logs()

    def _prepare_log_files(self) -> None:
        """Update log filenames with timestamps."""
        timestamp = datetime.now().strftime(self._settings['timestamp'])

        for handler in self._settings['handlers_to_file']:
            if handler not in self._config['handlers']:
                self.logger.warning('Skipping missing handler: %s', handler)
                continue

            self._config['handlers'][handler]['filename'] = str(
                self._log_dir
                / f"{timestamp}_{self._config['handlers'][handler]['filename']}"  # noqa: E501
            )

    def _cleanup_old_logs(self) -> None:
        """Remove old log files according to retention policy."""
        if not self._settings['enable_file_limit']:
            return

        for handler in self._settings['handlers_to_file']:
            try:
                _, prefix = handler.split('_', 1)
            except IndexError:
                self.logger.warning('Invalid handler name format: %s', handler)
                continue

            log_files = sorted(
                self._log_dir.glob(f'*_{prefix}.log'),
                key=lambda f: f.stat().st_ctime,
            )

            if len(log_files) > self._settings['max_log_files']:
                for file in log_files[: -self._settings['max_log_files']]:
                    try:
                        if not file.is_relative_to(self._log_dir):
                            self.logger.warning(
                                'Skipping external file: %s', file
                            )
                            continue

                        file.unlink()
                        self.logger.debug('Deleted old log: %s', file.name)
                    except Exception as e:
                        self.logger.exception('Error deleting %s: %s', file, e)
