"""Custom selections."""

from collections.abc import Iterable

import toga
from toga.sources import Listener
from toga.widgets.base import StyleT
from toga.widgets.detailedlist import SourceT


class SelectionApp(toga.Selection, Listener):
    """Custom selection widget."""

    def __init__(
        self,
        id: str | None = None,
        style: StyleT | None = None,
        items: SourceT | Iterable | None = None,
        accessor: str | None = None,
        value: object | None = None,
        on_change: toga.widgets.selection.OnChangeHandler | None = None,
        enabled: bool = True,
        on_select: None = None,  # DEPRECATED
    ) -> None:
        """Create a new Selection widget."""
        super().__init__(
            id, style, items, accessor, value, on_change, enabled, on_select
        )

    def set_value(self, value: object) -> None:
        """Set the initial value for the widget."""
        self.value = value


class BaseSelection(toga.Selection):
    """Custom selection widget.

    :param list[dict] items: Initial items to display for selection.
    :param value: Initial value for the selection.
    :type value: str or None.
    :param str accessor: The accessor to use to extract display values
        from the list of items.
    :param str alias: Key for attribute on the selected item.
    """

    def __init__(self, **kwargs: object) -> None:
        """Construct the widget."""
        kwargs['accessor'] = 'humanly'
        super().__init__(**kwargs)
        self.alias = 'alias'

    def set_items(self, items: list[dict], value: str | None) -> None:
        """Set selection initial items and initial value to display.

        :param list[dict] items: Initial items to display for selection.
        :param value: Initial value for the selection.
        :type value: str or None.
        """
        # Set Selection items attr.
        self.items = items
        # Set Selection value attr.
        for index, selection in enumerate(items):
            if selection[self.alias] == value:
                self.value = self.items[index]

    def get_items(self) -> list[dict[str, str]]:
        """Return items."""
        args = []
        for item in self.items:
            args.append({'alias': item.alias, 'humanly': item.humanly})
        return args

    def get_alias(self) -> str | int | list | None:
        """Get displayed value from selection."""
        return self.value.alias
