"""Application message."""

import toga


class MessageMixin:
    """Dialog message mixin."""

    app: toga.App

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct a dialog message."""
        super().__init__(*args, **kwargs)

    async def show_message(self, title: str, message: str) -> None:
        """Show dialog message."""
        await self.app.main_window.dialog(toga.InfoDialog(title, message))
