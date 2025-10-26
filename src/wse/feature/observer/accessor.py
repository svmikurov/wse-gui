"""Listener mixin via accessors."""

import toga


class AccessorMixin:
    """Listener via accessors."""

    _accessors: tuple[str, ...]

    def _check_accessors(self) -> None:
        """Check that UI attr name corresponding to accessor."""
        if not self._accessors:
            raise RuntimeError(
                f'Class `{self.__class__.__name__}` must define non-empty '
                f'`_accessors. Got: {self._accessors!r}`'
            )

        for accessor in self._accessors:
            self._has_accessor(f'_{accessor}')

    def _get_ui(self, accessor: str) -> toga.Widget:
        """Get UI via accessor."""
        try:
            return getattr(self, f'_{accessor}')  # type: ignore[no-any-return]

        except AttributeError:
            raise LookupError(
                f"Unknown accessor '{accessor}'. Available: {self._accessors}"
            ) from None

    def _has_accessor(self, accessor: str) -> None:
        if not hasattr(self, accessor):
            raise AttributeError(
                f"Not implemented attribute '{f'_{accessor}'}' in "
                f'`{self.__class__.__name__}` for observer pattern'
            )
