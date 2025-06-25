"""Multilingual internationalization service."""

import gettext
import logging
from pathlib import Path
from typing import Callable

from wse.config.enums import Language, LocaleDomain
from wse.config.settings import LANGUAGE, LOCALE_DOMAINS, RESOURCES_PATH
from wse.utils.interfaces import II18NService

logger = logging.getLogger(__name__)

LOCALEDIR = RESOURCES_PATH / 'locale'


class I18NService(II18NService):
    """Localization service."""

    def __init__(
        self,
        default_language: Language,
        locale_dir: Path,
        domains: list[LocaleDomain],
    ) -> None:
        """Construct the localization."""
        self._current_language = default_language
        self._locale_dir = locale_dir
        self._domains = domains

        # Setup service
        self._translators: dict[str, Callable[[str], str]] = {}
        self.set_language(self._current_language)

    def set_language(self, language: Language) -> None:
        """Switch to a specific language."""
        if language == self._current_language and not self._translators == {}:
            return

        new_translators = {}

        for domain in self._domains:
            try:
                trans = gettext.translation(
                    domain=domain,
                    localedir=self._locale_dir,
                    languages=[language],
                )
                new_translators[f'{domain}_'] = trans.gettext
                logger.debug(
                    f'Loaded "{language}" language for "{domain}" domain'
                )
            except Exception as e:
                logger.exception(
                    f'Error loading "{language}" localization '
                    f'for {domain} domain:\n%s',
                    e,
                )
                new_translators[f'{domain}_'] = (
                    gettext.NullTranslations().gettext
                )
                self._translators = {}

        self._translators = new_translators  # type: ignore[assignment]
        self._current_language = language

    def get_translator(self, domain: str) -> Callable[[str], str]:
        """Get translator function for a specific domain."""
        return self._translators[f'{domain}_']


# Create a singleton instance
i18n = I18NService(
    default_language=LANGUAGE,
    locale_dir=LOCALEDIR,
    domains=LOCALE_DOMAINS,
)


def nav_(text: str) -> str:
    """Get translated text for navigation button."""
    return i18n.get_translator(LocaleDomain.NAV)(text)


def label_(text: str) -> str:
    """Get translated text for label widget."""
    return i18n.get_translator(LocaleDomain.LABEL)(text)
