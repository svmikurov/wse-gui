"""Start app."""

from wse.core.logger.setup import setup_logging

setup_logging()

# ruff: noqa: E402
from wse.app import main

if __name__ == '__main__':
    main().main_loop()
