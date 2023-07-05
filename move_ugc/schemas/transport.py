"""Define gql transports for the client."""
from gql import Client
from gql.transport.requests import RequestsHTTPTransport
from pydantic import HttpUrl

from move_ugc.schemas.constants import AUTHORIZATION_HEADER


def _get_transport(endpoint_url: HttpUrl, api_key: str) -> RequestsHTTPTransport:
    """Get the transport for the GraphQL client.

    Args:
        endpoint_url: The endpoint URL to use for the transport.
        api_key: The API key to use for the transport.

    Returns:
        The transport for the GraphQL client.
    """
    return RequestsHTTPTransport(
        url=str(endpoint_url),
        use_json=True,
        headers={AUTHORIZATION_HEADER: api_key},
        verify=True,
    )


def _get_gql_client(transport: RequestsHTTPTransport) -> Client:
    """Get the GraphQL client.

    Args:
        transport: The transport to use for the client.

    Returns:
        The GraphQL client.
    """
    return Client(transport=transport, fetch_schema_from_transport=True)
