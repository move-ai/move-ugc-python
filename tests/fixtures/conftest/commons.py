"""Common fixtures for the UGC Client shared across types."""
from typing import Any, Dict

import pytest


@pytest.fixture
def metadata_for_update(faker) -> Dict[str, Any]:
    """Return metadata for update mutation across types.

    This metadata can be used to perform update mutation tests across types such as
    Job, File, Client, and Take etc.

    Args:
        faker (Faker): faker instance

    Returns:
        Dict[str, Any]: fake metadata dictionary
    """
    return faker.pydict()
