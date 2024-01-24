"""Client mixin for the Move UGC SDK."""
from typing import Any, Dict

from move_ugc.gql_requests.client import retrieve as retrieve_query
from move_ugc.gql_requests.client import update as update_query
from move_ugc.schemas.client import Client
from move_ugc.services.base import BaseService


class ClientService(BaseService[Client]):
    """Service which can be used to communicate with Client type in UGC API.

    To use this service, you need to instantiate it with a valid Move UGC client.

    ```python
    from move_ugc import MoveUgc
    ugc = MoveUgc(api_key="my-api-key")

    # Call client service methods directly
    ugc.clients.retrieve(id="client-<guid>")

    # Or use the client service as a mixin
    client_service = ugc.clients
    client_service.retrieve(id="client-<guid>")
    ```
    """

    _schema = Client

    def retrieve(self) -> Client:
        """Retrieve a client with given client_id from MoveUGC.

        Returns:
            Client instance of Pydantic model type.
        """
        return self.execute(
            query_key=retrieve_query.key,
            gql_query=retrieve_query.generate_query(),
        )

    def update(self, metadata: Dict[str, Any]) -> Client:
        """Update a client with given client_id from MoveUGC.

        Args:
            metadata (Dict[str, Any]): metadata to be updated.

        Returns:
            Client instance of Pydantic model type.
        """
        return self.execute(
            query_key=update_query.key,
            gql_query=update_query.generate_query(),
            variable_values={"metadata": self.encode_aws_metadata(metadata)},
        )
