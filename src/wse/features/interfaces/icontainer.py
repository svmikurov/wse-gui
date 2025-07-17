"""Defines protocols for widget containers interface."""

from typing import Protocol

from .._types import StyleT_co, ThemeT_co
from ..interfaces.icontent import IGetContent
from .iobserver import IObserver

# Protocols for container features


class IAddObserver(
    Protocol,
):
    """Protocol for add observer interface."""

    def add_observer(self, observer: IObserver) -> None:
        """Add a new observer to this subject."""


class ICreateNavButton(
    IAddObserver,
    Protocol,
):
    """Protocol for create navigation button interface."""


class IUpdateStyle(
    Protocol[StyleT_co, ThemeT_co],
):
    """Protocol for UI style updating interface."""

    def update_style(self, config: StyleT_co | ThemeT_co) -> None:
        """Update widgets style."""


class ILocalize(
    Protocol,
):
    """Protocol for UI localisation interface."""

    def localize_ui(self) -> None:
        """Localize the UI text."""


# Protocols for containers


class IContainer(
    IGetContent,
    Protocol,
):
    """Protocol for comon widget container interface."""


class StyledContainerABC(
    IContainer,
    IUpdateStyle[StyleT_co, ThemeT_co],
    Protocol,
):
    """Protocol for styled widget container interface."""


class LocaleContainerABC(
    StyledContainerABC[StyleT_co, ThemeT_co],
    ILocalize,
    Protocol,
):
    """Protocol for styled and localized widget container interface."""


class InteractiveContainer(
    IAddObserver,
    LocaleContainerABC[StyleT_co, ThemeT_co],
    Protocol,
):
    """Protocol for a container interface of interactive widgets."""


class INavigableContainer(
    ICreateNavButton,
    InteractiveContainer[StyleT_co, ThemeT_co],
    Protocol,
):
    """Protocol for navigation container interface."""
