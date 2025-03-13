"""Manages internationalization and language settings."""

import gettext
from pathlib import Path
from typing import Dict, Optional

import toga

from wse.config.config import PROJECT_PATH, Languages, Settings
from wse.core.logger import setup_logger

logger = setup_logger('language')


class I18N:
    """Handles translations and language settings."""

    current_lang: str = None
    translations: Dict[str, gettext.NullTranslations] = {}
    locale_dir: Path = PROJECT_PATH / 'src' / 'wse' / 'locales'
    _listeners: list[toga.Box] = []

    def __init__(self, settings: Optional[Settings] = None) -> None:
        """Construct the class."""
        super().__init__()
        self.settings = settings
        self._init_languages()
        self.set_language(settings.LANGUAGE)

    @classmethod
    def _init_languages(cls) -> None:
        """Initialize translations for all supported languages."""
        if not cls.translations:  # Загружаем только один раз
            for language in Languages:
                try:
                    cls.translations[language] = gettext.translation(
                        domain='app',
                        localedir=cls.locale_dir,
                        languages=[language],
                        fallback=True,
                    )
                except FileNotFoundError:
                    logger.warning(
                        f'Translation files for {language} not found.'
                    )
                    cls.translations[language] = gettext.NullTranslations()

    @classmethod
    def set_language(cls, lang: str) -> None:
        """Set the application language."""
        if lang in cls.translations:
            cls.current_lang = lang
            cls.translations[lang].install()
            logger.info(f'Language changed to: {lang}')
            cls.notify('language_changed')
        else:
            logger.warning(f'Unsupported language: {lang}')

    @classmethod
    def get_current_language(cls) -> str:
        """Get current language."""
        return cls.current_lang

    def gettext(self, text: str) -> str:
        """Return the translated text."""
        current_lang = self.__class__.current_lang
        if current_lang and current_lang in self.__class__.translations:
            return self.__class__.translations[current_lang].gettext(text)
        logger.warning(f'Language {current_lang} not configured.')
        return text

    @classmethod
    def notify(cls, notification: str, **kwargs: object) -> None:
        """Notify all listeners an event has occurred."""
        for listener in cls._listeners:
            try:
                method = getattr(listener, notification)
            except AttributeError:
                method = None

            if method:
                method(**kwargs)

    @classmethod
    def add_listener(cls, listener: toga.Box) -> None:
        """Add a new listener to this data source."""
        if listener not in cls._listeners:
            cls._listeners.append(listener)


# Global copy of translations
i18n = I18N(Settings())
_ = i18n.gettext
