"""Defines Swarm page model."""

import json

import httpx

import logging

from wse.features.base.mvc import BaseModel

logger = logging.getLogger(__name__)


class SwarmModel(BaseModel):
    """Swarm base model."""

    def perform_request(self, endpoint: str) -> None:
        """Request dat for info panel."""
        response = self.api_client.get(endpoint)
        text = self.format_pretty_json(response)
        self._notify_display_response(text)

    def _notify_display_response(self, text: str) -> None:
        """Display in text panel the http response."""
        self.subject.notify('display_data', text=text)

    # Utility methods
    @staticmethod
    def format_pretty_json(response: httpx.Response) -> str:
        json_text = response.json()
        pretty_json = json.dumps(json_text, indent=4, ensure_ascii=False)
        return pretty_json