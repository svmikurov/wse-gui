"""Abstract base classes for UI layout."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic

from ... import StyleT, ThemeT
from ...interfaces.icontent import ContentProto


class LocalizeABC(ABC):
    """ABC for UI localisation."""

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


class ContentABC(ABC):
    """ABC to provide content."""

    @property
    @abstractmethod
    def content(self) -> ContentProto:
        """Get page content.

        Returns the contents of a container or view.

        For example:

            class TopBarController:

                _container: ITopBarContainer

                @property
                def content(self) -> IContent:
                    return self._container.content
        """


@dataclass
class UpdateStyleABC(ABC, Generic[StyleT, ThemeT]):
    """ABC for UI style updating.

    Receives the style and theme configuration into the constructor.
    Provides functionality to apply the application style and theme to
    all widgets.

    :ivar StyleT _style: Widgets style config
    :ivar ThemeT _theme: Widgets thema config
    """

    _style: StyleT
    _theme: ThemeT

    def _apply_styles(self) -> None:
        self.update_style(self._style)
        self.update_style(self._theme)

    @abstractmethod
    def update_style(self, config: StyleT | ThemeT) -> None:
        """Update widgets style.

        For example:

        .. code-block:: python

            class SomeContainer(
                ContainerABC,
                UpdateStyleABC[TopBarStyle, TopBarTheme]
            ):

                _style: TopBarStyle
                _theme: TopBarTheme

                def _setup(self) -> None:
                    super()._setup()
                    self._apply_styles()

                def update_style(
                    self,
                    config: TopBarStyle | TopBarTheme
                ) -> None:
                    self._btn_back.style.update(**config.button)
                    self._label_balance.style.update(**config.label_balance)
                    ...
        """
