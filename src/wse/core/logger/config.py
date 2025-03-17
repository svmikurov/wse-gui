"""Logging configuration constants."""

from pathlib import Path

from wse.config.config import PROJECT_PATH

CONFIG_PATH: Path = PROJECT_PATH / 'src' / 'wse' / 'config' / 'logging.json'
LOG_DIR: Path = PROJECT_PATH / 'logs_src'
FALLBACK_LOG_PATH: Path = LOG_DIR / 'fallback.log'
