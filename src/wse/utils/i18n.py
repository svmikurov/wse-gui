"""Multilingual internationalization service."""

import gettext
import logging

from wse.config.settings import LANGUAGE, RESOURCES_PATH

logger = logging.getLogger('wse')

DOMAIN = 'nav'
LOCALEDIR = RESOURCES_PATH / 'locale'


try:
    trans = gettext.translation(
        domain=DOMAIN,
        localedir=LOCALEDIR,
        languages=[LANGUAGE],
    )
    _ = trans.gettext
    logger.info(f'Setup "{LANGUAGE}" language')
except Exception as e:
    # fallback by default
    _ = gettext.gettext
    logger.exception(f'Error to implement "{LANGUAGE}" localisation:\n%s', e)
