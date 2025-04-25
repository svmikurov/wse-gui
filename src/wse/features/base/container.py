"""Defines base widget container."""

from abc import ABC, abstractmethod
from typing import Type

import toga

from wse.features.shared.button import AppButton
from wse.features.shared.observer import Subject
from wse.features.shared.ui_containers import BaseContent
from wse.interface.ifeatures import IContent, ISubject


class BaseContainer(ABC):
    """Widget base container."""

    def __init__(
        self,
        content_box: IContent | None = None,
        subject: ISubject | None = None,
    ) -> None:
        """Construct the view."""
        # fmt: off
        self._content = content_box if content_box is not None else BaseContent()  # noqa: E501
        self._subject = subject if subject is not None else Subject()
        # fmt: on

        # Add UI
        self._create_ui()
        self.localize_ui()

    def _add_ui(self) -> None:
        """Add ui into content."""
        self.content.add(...)

    # UI create methods
    @abstractmethod
    def _create_ui(self) -> None:
        """Build a user interface."""

    @abstractmethod
    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""

    # Utility methods
    @property
    def subject(self) -> Subject:
        """Subject of observer pattern (read-only)."""
        return self._subject

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content

    @property
    def ui(self) -> list[toga.Widget]:
        """Return UI content widgets.

        For example:
        ------------

            class LoginView(...):
                ...
                def _add_ui(self):
                    self._content.add(
                        self._title,
                        *login_container.ui,
                        ...
                    )

        """
        return self.content.children


class NavigableContainer(BaseContainer, ABC):
    """Base navigable widget container."""

    BUTTON_CLASS: Type[toga.Button] = AppButton

    def _build_nav_btn(
        self,
        button_class: Type[toga.Button] | None = None,
        **kwargs: object,
    ) -> toga.Button:
        _cls = button_class or self.BUTTON_CLASS
        return _cls(on_press=self._handle_navigation, **kwargs)

    def _handle_navigation(self, button: toga.Button) -> None:
        self.subject.notify('navigate', nav_id=button.text)
