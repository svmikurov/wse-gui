"""UI layer exceptions."""

from typing import Any, Type

from wse.core.navigation import NavID


class ContentError(Exception):
    """Raised when unable to get or process page content."""


class RouteContentError(ContentError):
    """Raised when unable to get content by route."""

    def __init__(
        self,
        original_err: Exception,
        nav_id: NavID,
        routes_class: Type[Any],
    ) -> None:
        """Construct the exception."""
        help_message = (
            f'\nRoute mapping for `{nav_id}` was not set.\n'
            f'Add mapping `NavID` with Abstract Base Class of View '
            f'to {routes_class}\n\n'
            f'For example:\n\n'
            f'    class {routes_class.__name__}:\n'
            f'        def routes(self) -> dict[NavID, GetContentProto]:\n'
            f'            return {{\n'
            f'                ...\n'
            f'                NavID.TERMS: TermsViewABC,\n'
            f'                +++++++++++++++++++++++++\n'
            f'            }}\n\n'
            f'Original error: {type(original_err).__name__}: {original_err}'
        )
        super().__init__(help_message)


class PopulateContentError(ContentError):
    """Raised when unable to populate content."""

    def __init__(self, original_err: Exception) -> None:
        """Construct the exception."""
        message = (
            f'Populate content error:\n'
            f'Check that got content from injected widget.\n\n'
            f'For example:\n\n'
            f'  def _populate_content(self) -> None:\n'
            f'      self._content.add(\n'
            f'          self._top_bar.content,\n'
            f'                       ---------\n'
            f'      )\n\n'
            f'Original error: {type(original_err).__name__}: {original_err}'
        )
        super().__init__(message)
