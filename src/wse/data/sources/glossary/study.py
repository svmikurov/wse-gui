"""Glossary Term Presentation source."""

from wse.api.glossary import TermPresentationApiABC
from wse.api.glossary.schemas import TermPresentation
from wse.data.sources.base.source import AccessorSourceGen

from . import (
    PresentationAccessorT,
    PresentationNotifyT,
    TermPresentationListenerABC,
    TermPresentationNetworkSourceABC,
)


class TermPresentationNetworkSource(
    AccessorSourceGen[
        TermPresentationListenerABC,
        PresentationNotifyT,
        PresentationAccessorT,
    ],
    TermPresentationNetworkSourceABC,
):
    """Glossary Term Presentation source."""

    _presentation_api: TermPresentationApiABC

    def get_presentation(self) -> TermPresentation | None:
        """Fetch Term Presentation."""
