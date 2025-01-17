"""Controller of selected items list."""

import toga
from httpx import Response
from toga.sources import Source

from wse.contrib.data import to_entries
from wse.contrib.http_requests import request_delete_async, request_post
from wse.controllers.params import ControllerParams
from wse.sources.foreign import WordSource


class ConntrollerTable:
    """Controller of selected items list."""

    def __init__(self, plc_params: ControllerParams) -> None:
        """Construct the controller."""
        self._plc_params = plc_params

        # The pagination urls
        self._next_pagination_url = None
        self.current_pagination_url = None
        self._previous_pagination_url = None

        # To override
        self.source_url = ''
        self.source_url_detail = ''
        self.source_class = None
        self.headings = None

        # Sources
        self.entry = WordSource()
        self.event = Source()

    def on_open(self, widget: toga.Widget) -> None:
        """Request the items."""
        self.reset_pageination_urls()
        self.populate_table()

    ####################################################################
    # HTTP request

    def request_entries(
        self,
        pagination_url: str | None = None,
    ) -> list[tuple[str, ...]]:
        """Request the entries to populate the table."""
        lookup_conditions = self._plc_params.lookup_conditions
        # TODO: Refactor remove 'has_timeout', 'timeout', 'order'
        #  from lookup_conditions.
        lookup_conditions.pop('has_timeout')
        lookup_conditions.pop('timeout')
        lookup_conditions.pop('order')

        # Update pagination page if it, otherwise request first page.
        response = request_post(
            pagination_url or self.source_url,
            lookup_conditions,
        )

        # Set the pagination urls.
        self.set_pagination_urls(response)

        # Get entries to input at table.
        payload = response.json()
        entries = to_entries(payload['results'])
        return entries

    ####################################################################
    # Create, update, delete entry

    def create_handler(self, entry: object) -> None:
        """Update item."""
        pass

    def update_handler(self, entry: object) -> None:
        """Update item."""
        pass

    async def delete_handler(self, _: toga.Widget) -> None:
        """Delete the entry, button handler."""
        try:
            entry = self.table.selection
        except IndexError:
            print('DEBUG: The entry is empty')
        else:
            url = self.source_url_detail % entry.id
            await request_delete_async(url)
            self.populate_table(self.current_pagination_url)

    #####################################################################
    # Pagination

    def set_pagination_urls(self, response: Response) -> None:
        """Set pagination urls."""
        payload = response.json()
        self.next_pagination_url = payload['next']
        self.current_pagination_url = response.url
        self.previous_pagination_url = payload['previous']

    def reset_pageination_urls(self) -> None:
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

    #############################
    # Pagination buttons handlers

    def previous_handler(self, _: toga.Widget) -> None:
        """Populate the table by previous pagination, button handler."""
        self.populate_table(self.previous_pagination_url)

    def reload_handler(self, _: toga.Widget) -> None:
        """Update the table, button handler."""
        self.populate_table()

    def next_handler(self, _: toga.Widget) -> None:
        """Populate the table by next pagination, button handler."""
        self.populate_table(self.next_pagination_url)

    #####################################################################
    # Table

    def populate_table(self, url: str | None = None) -> None:
        """Populate the table on url request."""
        self.clear_table()
        entries = self.request_entries(url)
        for entry in entries:
            self.entry.add_entry(entry)

    def clear_table(self) -> None:
        """Clear the table."""
        self.entry.clear()
