"""Manages internationalization and language settings."""

import gettext
from typing import Any, Dict, Optional

from typing_extensions import Self

from wse.core.config import PROJECT_PATH, Languages, Settings
from wse.core.logger import setup_logger

logger = setup_logger('language')


class I18N:
    """Handles translations and language settings."""

    _instance: Optional['I18N'] = None
    translations: Dict[str, Any]
    current_lang: str
    locale_dir = PROJECT_PATH / 'src' / 'wse' / 'locales'

    def __new__(cls, settings: Optional[Settings] = None) -> Self:
        """Construct the class."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._init_languages()
            cls._instance._init_translations(settings)
        return cls._instance

    @classmethod
    def _init_languages(cls) -> None:
        """Initialize translations for all supported languages."""
        cls.translations = {}
        for language in Languages:
            cls.translations[language] = gettext.translation(
                domain='app',
                localedir=cls.locale_dir,
                languages=[language],
                fallback=True,
            )

    def _init_translations(self, settings: Optional[Settings]) -> None:
        """Initialize translations."""
        self.current_lang = settings.LANGUAGE if settings else Languages.EN
        self.translations[self.current_lang].install()

    def set_language(self, lang: str) -> None:
        """Set the application language."""
        if lang in self.translations:
            self.current_lang = lang
            self.translations[lang].install()
            logger.info(f'The application language is set to: {lang}')
        else:
            logger.warning(f'Unsupported language: {lang}')

    @classmethod
    def get_current_language(cls) -> str:
        """Get current language."""
        return cls._instance.current_lang if cls._instance else None

    def gettext(self, text: str) -> str:
        """Return the translated text."""
        if self.current_lang in self.translations:
            return self.translations[self.current_lang].gettext(text)
        else:
            logger.warning(
                f'Language {self.current_lang} not found in Translations'
            )
            return text


# Global copy of translations
i18n = I18N(Settings())
_ = i18n.gettext
