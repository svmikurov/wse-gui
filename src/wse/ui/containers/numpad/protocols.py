"""Protocols for numpad components and numpad observer."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.observer import SubjectABC
from wse.feature.observer.generic import SubjectGenABC
from wse.ui.base.container.abc import ContainerGenABC
from wse.ui.base.content.abc import GetContentABC

ModelNotifyT = Literal['numpad_input_updated']
ContainerNotifyT = Literal['button_pressed']
ControllerNotifyT = Literal['numpad_entered']


class NumPadObserverABC(ABC):
    """Protocol for num pad observer interface."""

    @abstractmethod
    def numpad_entered(self, value: str) -> None:
        """Notification about updating the entered value."""


class NumPadModelABC(
    SubjectABC,
    ABC,
):
    """Protocol for NumPad model interface."""

    @abstractmethod
    def update_input(self, value: str) -> None:
        """Update the user input."""

    @abstractmethod
    def clear_input(self) -> None:
        """Clear the entered data."""


class NumPadContainerABC(
    ContainerGenABC[StyleConfig, ThemeConfig],
    GetContentABC,
    SubjectABC,
    ABC,
):
    """Protocol for NumPad container interface."""

    @abstractmethod
    def update_enabled(self, enabled: bool) -> None:
        """Update buttons enabled features."""


class NumPadControllerABC(
    SubjectGenABC[NumPadObserverABC, ControllerNotifyT],
    GetContentABC,
    ABC,
):
    """Protocol for NumPad controller interface."""

    # Notification from View

    @abstractmethod
    def button_pressed(self, value: str) -> None:
        """Handle the button press event."""

    # Notification for outer component

    @abstractmethod
    def numpad_input_updated(self, value: str) -> None:
        """Handle the input update event."""

    # API for outer component

    @abstractmethod
    def clear_input(self) -> None:
        """Clear the entered data."""

    @abstractmethod
    def disable_buttons(self) -> None:
        """Disable numpad buttons."""

    @abstractmethod
    def enable_buttons(self) -> None:
        """Enable numpad buttons."""
