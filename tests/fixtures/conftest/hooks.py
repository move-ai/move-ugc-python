"""Implement hooks plugin to override global variables."""
import os

from move_ugc.settings import get_settings


def pytest_configure(config):
    """Override any global variable used in tests here.

    Args:
        config: The pytest config object.
    """
    # Clear cache
    get_settings.cache_clear()

    # Invalid value
    key = "PYTEST_INVALID"

    # Keys with specific syntax
    os.environ["move_ugc_endpoint_url"] = f"https://{key}_endpoint_url.com"

    # Generic keys to override
    keys_to_override = []
    for key_to_override in keys_to_override:
        os.environ[key_to_override] = f"move_{key}_{key_to_override}"
