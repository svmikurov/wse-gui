"""Defines a base params widgets."""

from abc import ABC, abstractmethod

import toga
from toga.style import Pack

from wse.features.shared.observer import Subject


class BaseParamsWidget(toga.Box, ABC):
    """Base container for params element."""

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__()
        self._source = source or Subject()

        # Style of the inner widget
        self._inner_style = Pack(padding=(2, 0, 2, 0))

        # Add UI
        self._create_ui()
        self._add_ui()

    @abstractmethod
    def _add_ui(self) -> None: ...

    @abstractmethod
    def _create_ui(self) -> None: ...
