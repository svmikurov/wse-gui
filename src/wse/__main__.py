"""Start app."""

import logging

from wse.app import main


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


if __name__ == '__main__':
    main().main_loop()
