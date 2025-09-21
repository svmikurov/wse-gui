"""Glossary Term Presentation source."""

from wse.feature.api.glossary import TermPresentationApiABC
from wse.feature.api.glossary.schema import TermPresentationSchema

from . import TermPresentationNetworkSourceABC


class TermPresentationNetworkSource(TermPresentationNetworkSourceABC):
    """Glossary Term Presentation source."""

    _presentation_api: TermPresentationApiABC

    def get_presentation(self) -> TermPresentationSchema | None:
        """Fetch Term Presentation."""
