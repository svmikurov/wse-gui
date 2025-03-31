import asyncio

import pytest


@pytest.fixture(scope="function")
def event_loop_policy():
    return asyncio.DefaultEventLoopPolicy()
