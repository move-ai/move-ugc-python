"""Client Type fixtures for the UGC Client."""
import json
from typing import Dict

import pytest
from graphql.execution.execute import ExecutionResult

from move_ugc.gql_requests.webhook_endpoint import add_webhook

FakeWebhookJson = Dict[str, Dict[str, str]]


@pytest.fixture
def fake_webhooks_type(webhooks_fixtures_path) -> FakeWebhookJson:
    """Fixture to return a fake webhooks type.

    Args:
        webhooks_fixtures_path (str): Path to webhooks fixtures.

    Returns:
        FakeWebhookJson: Fake webhooks type.
    """
    with open(f"{webhooks_fixtures_path}/fake_webhook_endpoint.json") as json_file:
        return json.load(json_file)


@pytest.fixture
def upsert_webhook_endpoint_response(
    mock_transport,
    fake_webhooks_type,
    introspection_result,
):
    """Fixture to return a fake webhook response for upsertWebhookEndpoint mutation.

    Args:
        mock_transport (MagicMock): Mock transport.
        fake_webhooks_type (dict[str, str]): Fake webhook json.
        introspection_result (dict[str, str]): Introspection result.

    Yields:
        webhook_response (ExecutionResult): Fake webhook response.
    """
    response = {add_webhook.key: fake_webhooks_type}
    webhook_response = ExecutionResult(data=response)
    mock_transport.side_effect = [introspection_result, webhook_response]
    yield webhook_response
