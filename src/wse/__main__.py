"""Start app."""

from wse.app import main
from wse.core.logger.setup import setup_logging

setup_logging()


if __name__ == '__main__':
    main().main_loop()
