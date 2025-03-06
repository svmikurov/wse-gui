"""Manages internationalization and language settings."""

import gettext
import os

from wse.core.logger import setup_logger

logger = setup_logger('language')


class I18N:
    """Handles translations and language settings."""

    _instance = None

    def __new__(cls) -> None:
        """Construct the class."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.init_translations()
        return cls._instance

    def init_translations(self) -> None:
        """Initialize translations."""
        self.locale_dir = os.path.join(os.path.dirname(__file__), 'locales')
        self.translations = {
            'en': gettext.translation(
                'app',
                self.locale_dir,
                languages=['en'],
            ),
            'ru': gettext.translation(
                'app',
                self.locale_dir,
                languages=['ru'],
            ),
        }
        self.current_lang = 'en'
        self.translations[self.current_lang].install()

    def set_language(self, lang: str) -> None:
        """Set the application language."""
        self.current_lang = lang
        self.translations[lang].install()
        logger.info(f'Setting application language to {lang}')

    def gettext(self, text: str) -> str:
        """Return the translated text."""
        return self.translations[self.current_lang].gettext(text)


# Global copy of translations
i18n = I18N()
_ = i18n.gettext
