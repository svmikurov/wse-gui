"""Defines exercise render."""

from wse.interface.iui.itext import IDisplayModel


class TextDisplayRenderer:
    """Exercise render."""

    @classmethod
    def render(cls, text: str, display: IDisplayModel) -> None:
        """Render the task."""
        display.clean()
        display.change(text)
