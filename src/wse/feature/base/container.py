"""Defines abstract base class for widget containers."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ...core.navigation.nav_id import NavID
from .. import StyleT, ThemeT
from ..base.mixins import (
    GetContentMixin,
)
from ..interfaces.iwidgets import NavigableButton
from ..shared.widgets.buttons import NavButton
from .abstract.mvc import LocalizeABC, UpdateStyleABC


@dataclass
class AddContentABC(
    GetContentMixin,
    ABC,
):
    """Abstract base class for widget container."""

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._setup()
        self._populate_content()

    def _setup(self) -> None:  # noqa: B027
        """Set up container features.

        Add features:
            - Content test ID
            - ...

        For example:

        .. code-block:: python

            def setup(self) -> None:
                self._content.test_id = NavID.HOME
                ...
        """
        pass

    @abstractmethod
    def _create_ui(self) -> None:
        """Create UI.

        For example:

        .. code-block:: python

            def _create_ui(self) -> None:
                self._label_title = toga.Label('')
                ...
        """

    @abstractmethod
    def _populate_content(self) -> None:
        """Populate widget container content with UI.

        For example:

        .. code-block:: python

            def _populate_content(self) -> None:
                self._content.add(
                    self._label_title,
                    ...,
                )
        """


@dataclass
class CreateNavButtonABC(ABC):
    """ABC for navigable container.

    For example:

        self._btn_account = self._create_nav_btn(nav_id=NavID.ACCOUNT)

        1) Use with observer pattern:

        _subject: Observable

        def _handle_navigate(self, button: NavigableButton) -> None:
            self._subject.notify('navigate', nav_id=button.nav_id)

        2) Use with callback of ViewModel method:

        def _handle_navigate(self, button: NavigableButton) -> None:
            self._state.navigate(button.nav_id)
    """

    def _create_nav_btn(self, nav_id: NavID) -> NavigableButton:
        """Create navigation button."""
        return NavButton(nav_id=nav_id, on_press=self._handle_navigate)

    @abstractmethod
    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press."""


class ContainerABC(
    UpdateStyleABC[StyleT, ThemeT],
    AddContentABC,
    LocalizeABC,
    ABC,
):
    """ABC for container."""

    def _setup(self) -> None:
        super()._setup()
        self.localize_ui()
        self._apply_styles()
