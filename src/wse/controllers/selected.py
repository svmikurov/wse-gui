"""Controller of selected items list."""

import toga
from httpx import Response
from toga.sources import Source

from wse.contrib.data import to_entries
from wse.contrib.http_requests import request_delete_async, request_get
from wse.controllers.params import ControllerParams


class Selected:
    """Controller of selected items list."""

    source_url: str
    source_url_detail: str
    source_class = None
    headings = None

    def __init__(self, plc_params: ControllerParams) -> None:
        """Construct the controller."""
        self.plc_params = plc_params
        # The pagination urls
        self._next_pagination_url = None
        self.current_pagination_url = None
        self._previous_pagination_url = None

        # Sources
        self.event = Source()

    def on_open(self, widget: toga.Widget) -> None:
        """Request the items."""
        pass

    ####################################################################
    # HTTP request

    def request_entries(
        self,
        pagination_url: str | None = None,
    ) -> list[tuple[str, ...]]:
        """Request the entries to populate the table."""
        # Update pagination page if it, otherwise request first page.
        response = request_get(pagination_url or self.source_url)

        # Set the pagination urls.
        self.set_pagination_urls(response)

        # Get entries to input at table.
        payload = response.json()
        entries = to_entries(payload['results'])
        return entries

    def set_pagination_urls(self, response: Response) -> None:
        """Set pagination urls."""
        payload = response.json()
        self.next_pagination_url = payload['next']
        self.current_pagination_url = response.url
        self.previous_pagination_url = payload['previous']

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

    ####################################################################
    # Create, update, delete entry

    def update_item(self, entry: object) -> None:
        """Update item."""
        pass

    async def delete_handler(self, _: toga.Widget) -> None:
        """Delete the entry, button handler."""
        try:
            entry = self.table.selection
        except IndexError:
            print('\nDEBUG: The entry is empty')
        else:
            url = self.source_url_detail % entry.id
            await request_delete_async(url)
            self.populate_table(self.current_pagination_url)
