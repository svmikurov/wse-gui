"""Listener mixin via accessors."""

import toga


class AccessorMixin:
    """Listener via accessors."""

    _accessors: tuple[str, ...]

    def _check_accessors(self) -> None:
        """Check that UI attr name corresponding to accessor."""
        if not self._accessors:
            raise AttributeError(
                f'Not implemented `_accessors` attribute in '
                f'`{self.__class__.__name__}` for observer pattern'
            )

        for attr in self._accessors:
            attr_name = f'_{attr}'

            if not hasattr(self, attr_name):
                raise AttributeError(
                    f"Not implemented attribute '{f'_{attr_name}'}' in "
                    f'`{self.__class__.__name__}` for observer pattern'
                )

    def _get_ui(self, accessor: str) -> toga.Widget:
        """Get UI via accessor."""
        try:
            return getattr(self, f'_{accessor}')  # type: ignore[no-any-return]

        except AttributeError:
            raise ValueError(
                f"Got unexpected accessor '{accessor}' for "
                f'`{self.__class__.__name__}`. Available: {self._accessors}'
            ) from None
