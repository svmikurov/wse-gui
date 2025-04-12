"""Defines login page view."""

from typing import Type, TypeVar

import toga
from toga.style import Pack

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.container import NavigableContainer
from wse.features.base.mvc import BaseNavigableView
from wse.features.shared.button import AppButton
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui_containers import ColumnBox
from wse.features.shared.ui_text import MultilineInfoPanel, TitleLabel

WidgetType = TypeVar('WidgetType', bound=toga.Widget)


class LoginContainer(NavigableContainer):
    """Login widgets container."""

    INPUT_HEIGHT = 60

    def __init__(self, *args: object, **kwarg: object) -> None:
        """Construct the container."""
        super().__init__(*args, **kwarg)

        # Add UI
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._username_input,
            self._password_input,
            self._btn_submit,
        )

    def _build_ui(self) -> None:
        self._username_input = self._build_input(toga.TextInput)
        self._password_input = self._build_input(toga.PasswordInput)
        self._btn_submit = AppButton(on_press=self._handel_submit)

    def localize_ui(self) -> None:
        self._username_input.placeholder = _('Username')
        self._password_input.placeholder = _('Password')
        self._btn_submit.text = _('Submit')

    # Button callback functions
    def _handel_submit(self, _: toga.Button) -> None:
        self.subject.notify('submit_login')

    # Utility methods
    def _build_input(self, class_input: Type[WidgetType]) -> WidgetType:
        return class_input(
            style=Pack(
                height=self.INPUT_HEIGHT,
            ),
        )


class LoginView(BaseNavigableView):
    """Login page view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.LOGIN

        # Login container
        self.login_container = LoginContainer(content_box=ColumnBox())

        # Add UI
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            self.info_panel,
            *self.login_container.get_content_widgets(),
            self._btn_back,
        )

    def _build_ui(self) -> None:
        """Create a user interface."""
        # Page title
        self._label_title = TitleLabel()

        # Info panel
        self.info_panel = MultilineInfoPanel()

        # Navigation buttons
        self._btn_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Assign a text for UI widgets."""
        # Page title
        self._label_title.text = _(NavigationID.LOGIN)

        # Navigate buttons
        self._btn_back.text = _(NavigationID.BACK)
