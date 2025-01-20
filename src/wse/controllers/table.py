"""Controller of selected items list."""

import toga
from httpx import Response
from toga.sources import Source

from wse.contrib.data import to_entries
from wse.contrib.http_requests import request_delete_async, request_post
from wse.controllers.params import ControllerParams
from wse.sources.source_list import SourceListApp


class ControllerTable:
    """Controller of selected items list."""

    source_url: str
    source_url_detail: str
    entry: SourceListApp

    def __init__(self, plc_params: ControllerParams) -> None:
        """Construct the controller."""
        self._plc_params = plc_params

        # Pagination urls
        self._next_pagination_url = None
        self.current_pagination_url = None
        self._previous_pagination_url = None

        # Page events source
        self.event = Source()

        # To override
        self.goto_create_handler = None
        self.goto_update_handler = None

    def on_open(self, widget: toga.Widget) -> None:
        """Request the items."""
        self._reset_pagination_urls()
        self._populate_table()

    ####################################################################
    # Create, update, delete handlers

    async def create_handler(self, widget: toga.Widget) -> None:
        """Go to create the term form, button handler."""
        await self.goto_create_handler(widget)

    async def update_handler(self, *args: object, **kwargs: object) -> None:
        """Update item."""
        await self.goto_update_handler(*args, **kwargs)

    async def delete_handler(self, _: toga.Widget, item_id: str) -> None:
        """Delete the entry, button handler."""
        url = self.source_url_detail % item_id
        await request_delete_async(url)
        self._populate_table(self.current_pagination_url)

    #####################################################################
    # Pagination handlers

    def previous_handler(self, _: toga.Widget) -> None:
        """Populate the table by previous pagination, button handler."""
        self._populate_table(self.previous_pagination_url)

    def reload_handler(self, _: toga.Widget) -> None:
        """Update the table, button handler."""
        self._populate_table()

    def next_handler(self, _: toga.Widget) -> None:
        """Populate the table by next pagination, button handler."""
        self._populate_table(self.next_pagination_url)

    ############################
    # Utility pagination methods

    def _set_pagination_urls(self, response: Response) -> None:
        """Set pagination urls."""
        payload = response.json()
        self.next_pagination_url = payload['next']
        self.current_pagination_url = response.url
        self.previous_pagination_url = payload['previous']

    def _reset_pagination_urls(self) -> None:
        """Reset pagination urls."""
        self.next_pagination_url = None
        self.current_pagination_url = None
        self.previous_pagination_url = None

    @property
    def next_pagination_url(self) -> str:
        """Next pagination url (`str`)."""
        return self._next_pagination_url

    @next_pagination_url.setter
    def next_pagination_url(self, value: str | None) -> None:
        self._next_pagination_url = value
        self.event.notify('update_next_button', is_active=bool(value))

    @property
    def previous_pagination_url(self) -> str:
        """Previous pagination url (`str`)."""
        return self._previous_pagination_url

    @previous_pagination_url.setter
    def previous_pagination_url(self, value: str | None) -> None:
        self._previous_pagination_url = value
        self.event.notify('update_previous_button', is_active=bool(value))

    #####################################################################
    # Table methods

    def _populate_table(self, url: str | None = None) -> None:
        """Populate the table on url request."""
        self._clear_table()
        entries = self._request_entries(url)
        for entry in entries:
            self.entry.append(entry)

    def _clear_table(self) -> None:
        """Clear the table."""
        self.entry.clear()

    ####################################################################
    # HTTP request

    def _request_entries(
        self,
        pagination_url: str | None = None,
    ) -> list[tuple[str, ...]]:
        """Request the entries to populate the table."""
        lookup_conditions = self._plc_params.lookup_conditions
        for key in ('order', 'timeout', 'has_timeout'):
            lookup_conditions.pop(key, None)

        # Update pagination page if it, otherwise request first page.
        response = request_post(
            pagination_url or self.source_url,
            lookup_conditions,
        )

        # Set the pagination urls.
        self._set_pagination_urls(response)

        # Get entries to input at table.
        payload = response.json()
        entries = to_entries(payload['results'])
        return entries
