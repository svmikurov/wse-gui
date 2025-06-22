"""Start app."""

from wse.core.logger import setup_logger

setup_logger()

from wse.app import main  # noqa: E402

if __name__ == '__main__':
    main().main_loop()
