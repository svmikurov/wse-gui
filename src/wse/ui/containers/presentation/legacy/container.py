"""Presentation container layout."""

from dataclasses import dataclass

import toga
from injector import inject

from wse.core.exceptions import NotImplementedAccessorError

from . import (
    AccessorT,
    PresentationContainerABC,
)


@inject
@dataclass
class PresentationContainer(
    PresentationContainerABC,
):
    """Presentaition container."""

    def __post_init__(self) -> None:
        """Construct the container."""
        super().__post_init__()
        self.accessors = ['case', 'text']
        for accessor in self.accessors:
            if not hasattr(self, '_' + accessor):
                raise NotImplementedAccessorError(accessor, self.__class__)

    def _create_ui(self) -> None:
        self._case = toga.Label('')
        self._text = toga.Label('')

    def _populate_content(self) -> None:
        self._content.add(
            self._case,
            self._text,
        )

    def update(self, accessor: AccessorT, value: object) -> None:
        """Change item value."""
        if accessor not in self.accessors:
            raise AttributeError(
                f"{self.__class__} have no '{accessor}' accessor"
            )
        attr: toga.Label = getattr(self, '_' + accessor)
        attr.text = value
