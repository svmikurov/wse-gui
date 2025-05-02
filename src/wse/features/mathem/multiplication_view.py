"""Defines Multiplication page view."""

import dataclasses

import toga
from toga.style import Pack

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.shared.object_id import ObjectID
from wse.features.shared.style_id import StyleID
from wse.interface.ifeatures import IContent
from wse.interface.iui.ibutton import IButtonFactory, IButtonHandler
from wse.interface.iui.ikeypad import IKeypad
from wse.interface.iui.itext import IDisplayPanel


@dataclasses.dataclass
class MultiplicationView:
    """Multiplication page view."""

    _content: IContent
    display_model: IDisplayPanel
    display_input: IDisplayPanel
    keypad: IKeypad
    _style_config: dict
    _button_factory: IButtonFactory
    button_handler: IButtonHandler

    def __post_init__(self) -> None:
        """Post init."""
        self._content.id = ObjectID.MULTIPLICATION
        self._layout_view()

    def _layout_view(self) -> None:
        self._create_ui()
        self._populate_content()
        self.update_ui_style()
        self.localize_ui()

    def _populate_content(self) -> None:
        self._content.add(
            self._title_label,
            self._question_label,
            self.display_model.content,
            self._answer_label,
            self.display_input.content,
            toga.Box(style=Pack(flex=1)),  # Flex stub
            self.keypad.content,
            self._answer_button,
            self._back_button,
        )

    def _create_ui(self) -> None:
        self._title_label = self._create_label()
        self._question_label = self._create_label()
        self._answer_label = self._create_label()
        self._answer_button = self._create_button()
        self._back_button = self._create_navigation_button()

    # Localize widget text

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._title_label.text = _('Multiplication title')
        self._question_label.text = _('Question')
        self._answer_label.text = _('Answer input')
        self._answer_button.text = _('Check answer')
        self._back_button.text = _(NavigationID.BACK)

    # Widget style

    @property
    def _ui_styles(self) -> dict[toga.Widget, StyleID]:
        return {
            self._title_label: StyleID.TITLE,
            self._question_label: StyleID.DEFAULT_LABEL,
            self._answer_label: StyleID.DEFAULT_LABEL,
            self._answer_button: StyleID.DEFAULT_BUTTON,
            self._back_button: StyleID.DEFAULT_BUTTON,
        }

    def update_ui_style(self) -> None:
        """Update widgets style."""
        style = self._style_config

        for widget, style_id in self._ui_styles.items():
            widget.style.update(**style.get(style_id))

        # UI with content has `update_style` method.
        self.display_model.update_style(style.get(StyleID.LINE_DISPLAY))
        self.display_input.update_style(style.get(StyleID.LINE_DISPLAY))

    # Utility methods

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content

    @staticmethod
    def _create_label() -> toga.Label:
        return toga.Label(text='')

    def _create_button(self) -> toga.Button:
        return self._button_factory.create(
            on_press=self.button_handler.button_press
        )

    def _create_navigation_button(self) -> toga.Button:
        return self._button_factory.create(
            on_press=self.button_handler.navigate
        )
