"""Defines abc for constructing mvc model component base classes."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic

from injector import inject

from ... import StyleT, ThemeT
from ...interfaces.icontent import IContent


class LocalizeABC(ABC):
    """Abstract base class for UI localisation."""

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
    """Abstract base class for providing content."""

    @property
    @abstractmethod
    def content(self) -> IContent:
        """Get page content.

        Returns the contents of a container or view.

        For example:

            class TopBarController:

                _container: ITopBarContainer

                @property
                def content(self) -> IContent:
                    return self._container.content
        """


@inject
@dataclass
class UpdateStyleABC(ABC, Generic[StyleT, ThemeT]):
    """Abstract base class for UI style updating.

    Receives the style and theme configuration into the constructor.
    Provides functionality to apply the application style and theme to
    all widgets.

    :ivar StyleT _style_config: Widgets style config DTO
    :ivar ThemeT _theme_config: Widgets thema config DTO
    """

    _style_config: StyleT
    _theme_config: ThemeT

    def _apply_styles(self) -> None:
        self.update_style(self._style_config)
        self.update_style(self._theme_config)

    @abstractmethod
    def update_style(self, config: StyleT | ThemeT) -> None:
        """Update widgets style.

        For example:

        .. code-block:: python

            class SomeContainer(
                ContainerABC,
                UpdateStyleABC[TopBarStyle, TopBarTheme]
            ):

                _style_config: TopBarStyle
                _theme_config: TopBarTheme

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
