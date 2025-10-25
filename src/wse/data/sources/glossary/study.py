"""Glossary Term Presentation source."""

from wse.data.sources.base.source import AccessorSourceGen
from wse.feature.api.glossary import TermPresentationApiABC
from wse.feature.api.glossary.schemas import TermPresentationSchema

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

    def get_presentation(self) -> TermPresentationSchema | None:
        """Fetch Term Presentation."""
