"""Defines Multiplication page view."""

import toga

from toga.style import Pack

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.shared.object_id import ObjectID
from wse.features.shared.style_id import StyleID
from wse.interface.ifeatures import IContent
from wse.interface.iui.ibutton import IButtonFactory, IButtonHandler
from wse.interface.iui.ikeypad import IKeypad
from wse.interface.iui.itext import IDisplay


class MultiplicationView:
    """Multiplication page view."""

    def __init__(
        self,
        content: IContent,
        model_display: IDisplay,
        input_display: IDisplay,
        keypad: IKeypad,
        style_config: dict,
        button_factory: IButtonFactory,
        button_handler: IButtonHandler,
    ) -> None:
        """Construct the view."""
        self._content = content
        self._model_display = model_display
        self._input_display = input_display
        self._keypad = keypad
        self._style_config = style_config
        self._button_factory = button_factory
        self.button_handler = button_handler

        self._content.id = ObjectID.MULTIPLICATION
        self._layout_view()

    def _layout_view(self) -> None:
        self._create_ui()
        self._populate_content()
        self.update_widget_style(self._style_config)
        self.localize_ui()

    def _populate_content(self) -> None:
        self._content.add(
            self._title_label,
            self._question_label,
            self._model_display.content,
            self._answer_label,
            self._input_display.content,
            toga.Box(style=Pack(flex=1)),  # Flex stub
            self._keypad.content,
            self._answer_button,
            self._back_button,
        )

    def _create_ui(self) -> None:
        self._title_label = toga.Label(text='')
        self._question_label = toga.Label(text='')
        self._answer_label = toga.Label(text='')
        self._answer_button = self._button_factory.create(
            on_press=self.button_handler.button_press
        )
        self._back_button = self._button_factory.create(
            on_press=self.button_handler.navigate
        )

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._title_label.text = _('Multiplication title')
        self._question_label.text = _('Question')
        self._answer_label.text = _('Answer input')
        self._answer_button.text = _('Check answer')
        self._back_button.text = _(NavigationID.BACK)

    def update_widget_style(self, style: dict) -> None:
        """Update widgets style."""
        for widget, style_id in self._widget_styles.items():
            widget.style.update(**style.get(style_id))

        self._model_display.update_style(style.get(StyleID.LINE_DISPLAY))
        self._input_display.update_style(style.get(StyleID.LINE_DISPLAY))

    @property
    def _widget_styles(self) -> dict[toga.Widget, StyleID]:
        return {
            self._title_label: StyleID.TITLE,
            self._question_label: StyleID.DEFAULT_LABEL,
            self._answer_label: StyleID.DEFAULT_LABEL,
            self._answer_button: StyleID.DEFAULT_BUTTON,
            self._back_button: StyleID.DEFAULT_BUTTON,
        }

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content
