"""Fixtures for syrupy snapshot tests."""
import pytest
from syrupy.extensions.json import JSONSnapshotExtension


@pytest.fixture
def snapshot_json(snapshot):
    """Fixture for syrupy snapshot tests for json snapshots.

    Args:
        snapshot: The syrupy snapshot fixture.

    Returns:
        The snapshot fixture with JSONSnapshotExtension as the default extension.
    """
    return snapshot.with_defaults(extension_class=JSONSnapshotExtension)
