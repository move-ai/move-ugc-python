"""Move UGC SDK client."""
from functools import cached_property

from gql import Client
from pydantic import BaseModel, Field, HttpUrl, SecretStr

from move_ugc.schemas.constants import MINIMUM_API_KEY_LENGTH
from move_ugc.schemas.transport import _get_gql_client, _get_transport  # noqa: WPS450
from move_ugc.settings import get_settings


def get_default_endpoint_url() -> HttpUrl:
    """Get the default endpoint URL.

    Returns:
        HttpUrl: Default endpoint URL.
    """
    return get_settings().ugc_endpoint_url


class MetaClient(BaseModel):
    """Move UGC SDK client."""

    api_key: SecretStr = Field(
        description="Move UGC API key",
        title="API key",
        min_length=MINIMUM_API_KEY_LENGTH,
    )
    endpoint_url: HttpUrl = Field(
        default_factory=get_default_endpoint_url,
        description="Move UGC API endpoint URL",
        title="Move UGC API endpoint URL",
    )

    @cached_property
    def ugc_api(self) -> Client:
        """Get the GraphQL client.

        Returns:
            Client: GraphQL client.
        """
        transport = _get_transport(
            endpoint_url=self.endpoint_url,
            api_key=self.api_key.get_secret_value(),
        )
        return _get_gql_client(transport=transport)
