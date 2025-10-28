"""Defines protocol for style interfaces."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Protocol

from wse.config.layout import StyleConfig, ThemeConfig
from wse.types import StyleT, ThemeT


class StyleProto(Protocol):
    """Protocol for Style interface."""

    def update(self, **kwargs: object) -> None:
        """Update component style."""

    @property
    def direction(self) -> str:
        """The widget`s style direction."""

    @direction.setter
    def direction(self, value: str) -> None: ...


class StyledABC(Protocol):
    """Protocol for style interface."""

    @property
    def style(self) -> StyleProto:
        """The widget`s style."""

    @style.setter
    def style(self, style: StyleProto) -> None: ...


@dataclass
class UpdateStyleGenABC(ABC, Generic[StyleT, ThemeT]):
    """ABC for UI style updating.

    Receives the style and theme configuration into the constructor.
    Provides functionality to apply the application style and theme to
    all widgets.

    :ivar StyleT _style: Widgets style config
    :ivar ThemeT _theme: Widgets theme config
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


@dataclass
class StyleABC(ABC):
    """ABC for UI style updating.

    Call ``_apply_styles`` method into derived class.
    """

    _style: StyleConfig
    _theme: ThemeConfig

    def _apply_styles(self) -> None:
        self._update_style(self._style)
        self._update_style(self._theme)

    @abstractmethod
    def _update_style(self, config: StyleConfig | ThemeConfig) -> None: ...
