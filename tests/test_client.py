"""Unit tests for the creating a client."""

import pytest

from move_ugc import MoveUgc


class TestMoveUgcClient:
    """Test client class."""

    def test_create_client(self, faker, snapshot):
        """Test creating a client.

        Args:
            faker: The faker fixture.
            snapshot: The snapshot fixture.
        """
        client = MoveUgc(api_key=faker.pystr())
        assert client == snapshot

    def test_create_without_api_key(self, snapshot):
        """Test creating a client without an API key.

        Args:
            snapshot: The snapshot fixture.
        """
        with pytest.raises(ValueError, match="api_key"):
            MoveUgc(api_key="")
