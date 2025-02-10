"""Rig service for move-ugc-python-sdk."""
from move_ugc.gql_requests.rig import list_query
from move_ugc.schemas.commons import ListBaseItems
from move_ugc.schemas.rig import Rig
from move_ugc.services.base import BaseService


class RigService(BaseService[Rig]):
    """Service which can be used to communicate with Rig in UGC API.

    To use this service, you need to instantiate it with a valid Move UGC client.

    python
    from move_ugc import MoveUgc
    ugc = MoveUgc(api_key="my-api-key")

    # Call rig service methods directly
    ugc.rigs.list()
    """

    _schema = Rig
    _list_base_schema = ListBaseItems

    def list(
        self,
    ) -> ListBaseItems:
        """List Rig in MoveUGC.

        Returns:
            ListBaseItems: List of Rig instances of Pydantic model type.
        """
        return self.execute(  # type: ignore[return-value]
            query_key=list_query.key,
            gql_query=list_query.generate_query(),
            multi=True,
        )
