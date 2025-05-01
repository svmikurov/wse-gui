"""Defines Multiplication page view."""

import toga

from toga.style import Pack

from wse.core.i18n import _
from wse.features.shared.object_id import ObjectID
from wse.interface.ifeatures import IContent
from wse.interface.iobserver import ISubject
from wse.interface.iui.ikeypad import IKeypad
from wse.interface.iui.itext import IDisplay


class MultiplicationView:
    """Multiplication page view."""

    def __init__(
        self,
        content: IContent,
        subject: ISubject,
        model_display: IDisplay,
        input_display: IDisplay,
        keypad: IKeypad,
        style_config: dict,
    ) -> None:
        """Construct the view."""
        self._content = content
        self._subject = subject
        self._model_display = model_display
        self._input_display = input_display
        self._keypad = keypad
        self._style = style_config

        self._content.id = ObjectID.MULTIPLICATION
        self._layout_view()

    def _layout_view(self) -> None:
        self._create_ui()
        self._populate_content()
        self.update_style()
        self.localize_ui()

    def _create_ui(self) -> None:
        self._title_label = toga.Label(text='')
        self._question_label = toga.Label(text='')
        self._answer_label = toga.Label(text='')

    def _populate_content(self) -> None:
        self._content.add(
            self._title_label,
            self._question_label,
            self._model_display.content,
            self._answer_label,
            self._input_display.content,
            toga.Box(style=Pack(flex=1)),
            self._keypad.content,
        )

    def update_style(self, to_style: dict | None = None) -> None:
        style = to_style if to_style is not None else self._style

        self._title_label.style.update(**style.get('Title'))
        self._question_label.style.update(**style.get('Label default'))
        self._answer_label.style.update(**style.get('Label default'))
        self._model_display.update_style(style.get('Single line display'))
        self._input_display.update_style(style.get('Single line display'))

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._title_label.text = _('Multiplication title')
        self._question_label.text = _('Question')
        self._answer_label.text = _('Answer input')


    @property
    def subject(self) -> ISubject:
        """Model subject (read-only)."""
        return self._subject

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content
