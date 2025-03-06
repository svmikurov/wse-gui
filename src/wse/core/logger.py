"""Logging settings."""

import logging
from typing import Optional


def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    """Set up the logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Log format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Logs to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Logs to file (optional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


root_logger = setup_logger('wse')
