"""Defines context managers."""

import toga


class EventDisabler:
    """Temporary disabled `on_change` method of `toga.Selection` widget.

    For example:

        def update_exercise_select(
            self, exercises: list[Exercise],
        ) -> None:
            with EventDisabler(self._exercise_select):
                self._exercise_select.items.update(exercises)
    """

    def __init__(self, widget: toga.Selection) -> None:
        """Construct the context manage."""
        self._widget = widget
        self._widget_handler = None

    def __enter__(self) -> None:
        """Disable widget handler."""
        self._widget_handler = self._widget.on_change
        self._widget.on_change = None

    def __exit__(self, *args: object) -> None:
        """Enable widget handler."""
        self._widget._on_change = self._widget_handler
