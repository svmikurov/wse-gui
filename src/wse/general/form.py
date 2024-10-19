"""Form classe."""

from wse.general.data import ManagingWidgetDataFromResponse
from wse.page.base import BaseBox


class BaseForm(
    BaseBox,
    ManagingWidgetDataFromResponse,
):
    """Base form widget class."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the form."""
        super().__init__(*args, **kwargs)

    def on_open(self) -> None:
        """Invoke the focus to input field on open form."""
        self.focus_to_input_field()