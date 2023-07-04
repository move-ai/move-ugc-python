"""Client Type fixtures for the UGC Client."""
import json

import pytest


@pytest.fixture
def fake_client_type(client_fixtures_path):
    """Fixture to return a fake client type.

    Args:
        client_fixtures_path (str): Path to client fixtures.

    Returns:
        dict: Fake client type.
    """
    with open(f"{client_fixtures_path}/fake_client_type.json") as json_file:
        return json.load(json_file)
