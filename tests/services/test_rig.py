"""Unit tests for using the rig service."""

from tests.services.testcases import ServicesTestCase


class TestRigService(ServicesTestCase):
    """Test rig service."""

    service_name = "rigs"

    def test_list(self, snapshot, rig_list_response):
        """Test listing rig.

        This should test -> `ugc.rig.list()`

        Args:
            snapshot (SnapshotFixture): Pytest snapshot fixture.
            rig_list_response (dict): Rig list response.
        """
        rig_list = self.client.rigs.list()
        self.assert_execute(snapshot, name="rig_list_request")
        snapshot.assert_match(
            rig_list.model_dump(),
            name="list_response",
        )
