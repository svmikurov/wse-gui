"""Text styled widgets."""

import toga
from toga.constants import CENTER
from toga.style import Pack

from wse.features.settings import TITLE_LABEL_FONT_SIZE, TITLE_LABEL_PADDING
from wse.features.shared.observer import TextListenerMixin, ValueListenerMixin
from wse.interface.ifeatures import IContent


class TitleLabel(toga.Label):
    """Heading label with preset style.

    The style (font, alignment, indents) is already defined.
    """

    TEXT_ALIGN = CENTER
    FONT_SIZE = TITLE_LABEL_FONT_SIZE
    PADDING = TITLE_LABEL_PADDING

    def __init__(self, text: str = '', **kwargs: object) -> None:
        """Construct the label."""
        super().__init__(text=text, **kwargs)
        self.style.text_align = self.TEXT_ALIGN
        self.style.font_size = self.FONT_SIZE
        self.style.padding = self.PADDING


class LabelParam(toga.Label):
    """Styled label of parameters."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the style of label."""
        super().__init__(*args, **kwargs)
        self.style.padding = (7, 0, 7, 2)


class TextPanel(ValueListenerMixin, toga.MultilineTextInput):
    """Text panel for info display."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        kwargs.setdefault('value', '')
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.readonly = True


class TextInLinePanel(TextListenerMixin, toga.Label):
    """In-line text panel for text display with changes."""

    def __init__(self, text: str = '', **kwargs: object) -> None:
        """Construct the text line panel."""
        super().__init__(text, **kwargs)
        self.style.flex = 1


class TextPanelScroll(toga.ScrollContainer):
    """Text panel with horizontal scroll."""

    _PANEL_WIDTH = 1000

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the panel."""
        super().__init__(*args, **kwargs)
        self.style.flex = 1
        self.content = toga.MultilineTextInput(
            style=Pack(
                flex=1,
                width=self._PANEL_WIDTH,
            ),
            readonly=True,
        )

    def change(self, value: str) -> None:
        """Update text widget value."""
        self.content.value = value

    def clean(self) -> None:
        """Clear the value of the text widget."""
        self.content.value = ''


class LineDisplay:
    """Provides a single line display."""

    def __init__(
        self,
        content: IContent,
        style_config: dict,
    ) -> None:
        """Construct the display."""
        self._content = content
        self._style_config = style_config

        self._create_ui()
        self._populate_content()

    def _create_ui(self) -> None:
        self._display = toga.Label('Display')

    def _populate_content(self) -> None:
        self._content.add(
            self._display,
        )

    def update_style(self, value: dict) -> None:
        """Update UI style."""
        self._display.style.update(**value)

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content
