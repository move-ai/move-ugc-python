"""Json fixtures."""

import os

import pytest


@pytest.fixture
def json_fixtures_path():
    """Fixture to return the path to the JSON fixtures.

    Returns:
        str: Path to JSON fixtures.
    """
    return os.path.join(os.path.dirname(__file__), "..", "json")


@pytest.fixture
def files_fixtures_path(json_fixtures_path):
    """Fixture to return the path to the files fixtures.

    Args:
        json_fixtures_path (str): Path to JSON fixtures.

    Returns:
        str: Path to files fixtures.
    """
    return os.path.join(json_fixtures_path, "file")


@pytest.fixture
def client_fixtures_path(json_fixtures_path):
    """Fixture to return the path to the client fixtures.

    Args:
        json_fixtures_path (str): Path to JSON fixtures.

    Returns:
        str: Path to client fixtures.
    """
    return os.path.join(json_fixtures_path, "client")


@pytest.fixture
def take_fixtures_path(json_fixtures_path):
    """Fixture to return the path to the take fixtures.

    Args:
        json_fixtures_path (str): Path to JSON fixtures.

    Returns:
        str: Path to take fixtures.
    """
    return os.path.join(json_fixtures_path, "take")


@pytest.fixture
def job_fixtures_path(json_fixtures_path):
    """Fixture to return the path to the job fixtures.

    Args:
        json_fixtures_path (str): Path to JSON fixtures.

    Returns:
        str: Path to job fixtures.
    """
    return os.path.join(json_fixtures_path, "job")


@pytest.fixture
def webhooks_fixtures_path(json_fixtures_path):
    """Fixture to return the path to the webhooks fixtures.

    Args:
        json_fixtures_path (str): Path to JSON fixtures.

    Returns:
        str: Path to webhooks fixtures.
    """
    return os.path.join(json_fixtures_path, "webhooks")


@pytest.fixture
def volume_fixtures_path(json_fixtures_path):
    """Fixture to return the path to the volume fixtures.

    Args:
        json_fixtures_path (str): Path to JSON fixtures.

    Returns:
        str: Path to volume fixtures.
    """
    return os.path.join(json_fixtures_path, "volume")


@pytest.fixture
def camera_settings_fixtures_path(json_fixtures_path):
    """Fixture to return the path to the camera settings fixtures.

    Args:
        json_fixtures_path (str): Path to JSON fixtures.

    Returns:
        str: Path to camera settings fixtures.
    """
    return os.path.join(json_fixtures_path, "camera_settings")
