"""Manages internationalization and language settings."""

import gettext
from pathlib import Path
from typing import Any, Dict, Optional

from wse.core.config import PROJECT_PATH, Language, Settings
from wse.core.logger import setup_logger

logger = setup_logger('language')


class I18N:
    """Handles translations and language settings."""

    _instance: Optional['I18N'] = None
    locale_dir: Path
    translations: Dict[str, Any]
    current_lang: str

    def __new__(cls, settings: Optional[Settings] = None) -> None:
        """Construct the class."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.init_translations(settings)
        return cls._instance

    def init_translations(self, settings: Optional[Settings]) -> None:
        """Initialize translations."""
        self.locale_dir = PROJECT_PATH / 'src' / 'wse' / 'locales'
        self.translations = {
            Language.EN: gettext.translation(
                'app',
                self.locale_dir,
                languages=[Language.EN],
                fallback=True,
            ),
            Language.RU: gettext.translation(
                'app',
                self.locale_dir,
                languages=[Language.RU],
                fallback=True,
            ),
        }
        self.current_lang = settings.LANGUAGE if settings else Language.EN
        self.translations[self.current_lang].install()

    def set_language(self, lang: str) -> None:
        """Set the application language."""
        if lang in self.translations:
            self.current_lang = lang
            self.translations[lang].install()
            logger.info(f'Установлен язык приложения: {lang}')
        else:
            logger.warning(f'Неподдерживаемый язык: {lang}')

    def gettext(self, text: str) -> str:
        """Return the translated text."""
        return self.translations[self.current_lang].gettext(text)


# Global copy of translations
i18n = I18N(Settings())
_ = i18n.gettext
