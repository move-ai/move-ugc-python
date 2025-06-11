"""Common testcases for services."""

import pytest
from graphql import DocumentNode
from graphql.language.printer import print_ast


@pytest.mark.usefixtures("mock_client", "mock_transport")
class ServicesTestCase:
    """Test case for services."""

    service_name: str

    def test_fetch_service(self, snapshot):
        """Test fetching the service from the client.

        This test validates whether the service can be accessed from the client.

        Args:
            snapshot: The snapshot fixture.
        """
        service = getattr(self.client, self.service_name)
        snapshot.assert_match(service)

    def assert_execute(self, snapshot, name):
        """Assert the execute method.

        Args:
            snapshot: The snapshot fixture.
            name: The snapshot name.
        """
        assert self.mock_execute.called
        call_args = self.mock_execute.call_args
        args, kwargs = call_args[0], call_args[1]
        readable_args = []
        for arg in args:
            if isinstance(arg, DocumentNode):
                # DocumentNode is not serializable in snapshots, hence convert to str.
                readable_args.append(print_ast(arg))
                continue
            readable_args.append(arg)
        assert snapshot(name=name) == [readable_args, kwargs]
