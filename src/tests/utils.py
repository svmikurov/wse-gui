"""Utils for testing."""

import asyncio
import json
import os
import pathlib
from http import HTTPStatus

from wse.app import WSE


def run_until_complete(wse: WSE) -> object:
    """Run the event loop until a Future is done."""
    time_to_sleep = 0.1
    return wse.loop.run_until_complete(asyncio.sleep(time_to_sleep))


class FixtureReader:
    """Reader of fixtures.

    Use to reade fixture for http response.
    """

    module_dir = pathlib.Path(__file__).parent

    def __init__(
        self,
        fixture_file_name: str,
        status_code: int = HTTPStatus.OK,
    ) -> None:
        """Construct the reader."""
        self.fixture = fixture_file_name
        self.status_code = status_code

    @property
    def fixture_path(self) -> str:
        """Return the path to fixture (`str`, reade-only)."""
        return os.path.join(self.module_dir, f'fixtures/{self.fixture}')

    @staticmethod
    def url() -> str:
        """Stub to return the url for http response fixture."""
        return 'NOTE: url stub from FixtureReader'

    def json(self) -> dict:
        """Return the data from http response fixture."""
        with open(self.fixture_path, 'r') as file:
            data = json.load(file)
        return data
