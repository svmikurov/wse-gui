"""Defines protocols for utility components interfaces."""

from typing import Callable, Protocol

from wse.config.enums import Language


class I18NServiceProto(Protocol):
    """Localization service.

    For example:

        i18n = I18NService(
            default_language=LANGUAGE,
            locale_dir=LOCALEDIR,
            domains=LOCALE_DOMAINS,
        )

        def nav_(text: str) -> str:
            return i18n.get_translator('nav')(text)

        text = nav_('text to localize')

    """

    def set_language(self, language: Language) -> None:
        """Switch to a specific language."""

    def get_translator(self, domain: str) -> Callable[[str], str]:
        """Get translator function for a specific domain."""
