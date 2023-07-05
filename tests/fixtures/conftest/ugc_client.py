"""Fixtures for the UGC Client."""
import pytest

from move_ugc import MoveUgc


@pytest.fixture
def mock_client(request, faker):
    """Mock the client.

    Args:
        request: The pytest request object.
        faker: The faker fixture.

    Yields:
        client: The mocked client.
    """
    client = MoveUgc(api_key=faker.pystr())
    if request.cls is not None:
        request.cls.client = client
    yield client
