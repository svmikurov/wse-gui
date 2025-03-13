"""Multilingual internationalization service."""

import gettext
from pathlib import Path
from typing import Dict

from wse.config.config import PROJECT_PATH, Languages, Settings
from wse.core.logger import setup_logger
from wse.interfaces.icore import II18NService

logger = setup_logger('I18NService')

DOMAIN = 'app'
LOCALE_DIR = PROJECT_PATH / 'src' / 'wse' / 'locales'


class I18NService(II18NService):
    """Handles translations and language settings."""

    def __init__(self, settings: Settings) -> None:
        """Construct the translations."""
        self.settings = settings
        self.current_lang: str = settings.langauge_config.LANGUAGE
        self.translations: Dict[str, gettext.NullTranslations] = {}
        self.locale_dir: Path = LOCALE_DIR
        self._listeners = []
        self._load_translations()

    def _load_translations(self) -> None:
        """Load translations for all supported languages."""
        lang: Languages
        for lang in Languages:
            try:
                self.translations[lang.value] = gettext.translation(
                    DOMAIN,
                    localedir=self.locale_dir,
                    languages=[lang.value],
                    fallback=True,
                )
            except FileNotFoundError:
                logger.warning(f'Translation files for "{lang}" not found.')
                self.translations[lang.value] = gettext.NullTranslations()

    def set_language(self, lang: Languages) -> bool:
        """Set application language."""
        if lang not in self.translations:
            logger.warning(f'Unsupported language: "{lang}"')
            return False

        if lang == self.current_lang:
            return False

        self.current_lang = lang
        self.translations[lang].install()
        self._notify_listeners()
        logger.info(f'Application language changed to: "{lang}"')
        return True

    def change_language(self, lang: Languages) -> None:
        """Change and persist language setting."""
        if self.set_language(lang):
            self.settings.langauge_config.LANGUAGE = lang
            self.settings.langauge_config.save()

    def get_current_language(self) -> str:
        """Get current language code."""
        return self.current_lang

    def gettext(self, text: str) -> str:
        """Translate text."""
        return self.translations[self.current_lang].gettext(text)

    def add_listener(self, listener: object) -> None:
        """Add listener for language changes."""
        if listener not in self._listeners:
            self._listeners.append(listener)

    def _notify_listeners(self) -> None:
        """Notify all listeners about language change."""
        for listener in self._listeners:
            if hasattr(listener, 'update_ui_texts'):
                listener.update_ui_texts()
