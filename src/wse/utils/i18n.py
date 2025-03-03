"""Language setting."""

import gettext
import os


class I18N:
    """Language setting."""

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
        """Set the langauge."""
        self.current_lang = lang
        self.translations[lang].install()

    def gettext(self, text: str) -> str:
        """Return translation."""
        return self.translations[self.current_lang].gettext(text)


# Global copy of translations
i18n = I18N()
_ = i18n.gettext
