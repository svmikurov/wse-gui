"""Abstract Base Class for localization.

**DEPRECATED**
"""

from abc import ABC, abstractmethod


# TODO: Remove ABC
class LocalizeABC(ABC):
    """ABC for UI localization."""

    @abstractmethod
    def localize_ui(self) -> None:
        """Localize the UI text.

        For example:

        .. code-block:: python

            def _setup(self) -> None:
                super()._setup()
                self.localize_ui()

            def localize_ui(self) -> None:
                self._label_title.text = label_('Home page title')
                ...
        """
