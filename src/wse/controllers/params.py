"""Exercise parameters logic."""

from http import HTTPStatus

import toga

from wse.contrib.http_requests import request_get, request_put_async
from wse.source.number_input import SourceDecimal
from wse.source.selection import SourceSelections
from wse.source.switch import SourceProgressArray, SourceSwitch

ACCESSORS = ['alias', 'name']


class ParamsSources:
    """Exercise params sources."""

    def __init__(self) -> None:
        """Construct param sources."""
        super().__init__()

        # Selection
        self.category = SourceSelections(ACCESSORS)
        self.source = SourceSelections(ACCESSORS)
        self.order = SourceSelections(ACCESSORS)
        self.period_start_date = SourceSelections(ACCESSORS)
        self.period_end_date = SourceSelections(ACCESSORS)

        # Decimal
        self.count_first = SourceDecimal()
        self.count_last = SourceDecimal()
        self.timeout = SourceDecimal()

        # Bool
        self.favorites = SourceSwitch()
        self.is_first = SourceSwitch()
        self.is_last = SourceSwitch()
        self.has_timeout = SourceSwitch()

        # Progress array
        self.progress = SourceProgressArray()


class ParamsController(ParamsSources):
    """Exercise params controller."""

    def __init__(self) -> None:
        """Construct the exercise params."""
        super().__init__()
        self._url: str | None = None
        self._exercise_choices: dict | None = None
        self._default_values: dict | None = None
        self._lookup_conditions: dict | None = None

    async def on_open(self, _: toga.Widget) -> None:
        """Request exercise params and populate selections."""
        if not self._exercise_choices:
            await self.update_params()

    async def update_params(self) -> None:
        """Request exercise params from server."""
        params = self._request_params()

        if params:
            self._set_requested_params(params)
            self._populate_selections()
            self._set_default_params()
        else:
            # TODO: Add message.
            pass

    def _set_requested_params(self, params: dict) -> None:
        """Set exercise params for selection task as attr."""
        self._exercise_choices = params['exercise_choices']
        self._default_values = params['default_values']
        self._lookup_conditions = params['lookup_conditions']

    def _populate_selections(self) -> None:
        """Populate the selections with the choices."""
        for name, value in self._exercise_choices.items():
            # Exercise choices of progress are array.
            if name not in ('progress'):
                attr = getattr(self, name)
                attr.update_data(value)

    def _set_default_params(self) -> None:
        """Set default params."""
        self._set_params(self._default_values)

    def set_saved_params(self) -> None:
        """Set saved params."""
        self._set_params(self._lookup_conditions)

    def _set_params(self, data: dict) -> None:
        """Set params as attr."""
        for name, value in data.items():
            attr = getattr(self, name)
            attr.set_value(value)

    ####################################################################
    # HTTP requests

    def set_url(self, url: str) -> None:
        """Set params url."""
        self._url = url

    def _request_params(self) -> dict | None:
        """Request a exercise params."""
        response = request_get(self._url)
        if response.status_code == HTTPStatus.OK:
            return response.json()

    async def request_save_lookup_conditions(self) -> None:
        """Request to save user lookup conditions."""
        lookup_conditions = {}

        for name in self._lookup_conditions.keys():
            attr = getattr(self, name)
            lookup_conditions[name] = attr.get_value()

        await request_put_async(url=self._url, payload=lookup_conditions)
