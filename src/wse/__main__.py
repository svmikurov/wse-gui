"""Start the application."""

from wse.core.logger import setup_logger
from wse.main import main

logger = setup_logger('__main__')


if __name__ == '__main__':
    app = main()
    if app:
        app.main_loop()
    else:
        logger.error('Failed to initialize application')
