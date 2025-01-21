"""Form class."""

import toga

from wse.pages.widgets.box_page import WidgetMixin
from wse.pages.widgets.data import HandleSuccessResponse


class BaseForm(
    WidgetMixin,
    HandleSuccessResponse,
):
    """Base form widget class."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the form."""
        super().__init__(*args, **kwargs)

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke the focus to input field on open form."""
        self.focus_to_input_field()
