"""Take service for Move UGC SDK."""
from typing import Any, Dict, List, Optional

from move_ugc.gql_requests.take import create as create_query
from move_ugc.gql_requests.take import create_multicam, list_query
from move_ugc.gql_requests.take import retrieve as retrieve_query
from move_ugc.gql_requests.take import update as update_query
from move_ugc.schemas.commons import ListBase, SortDirection, get_default_page_size
from move_ugc.schemas.constants import ALLOWED_EXPAND_ATTRS
from move_ugc.schemas.sources import SourceIn
from move_ugc.schemas.sync_method import SyncMethodInput
from move_ugc.schemas.take import TakeType
from move_ugc.services.base import BaseService


class TakeService(BaseService[TakeType]):
    """Service which can be used to communicate with Take type in UGC API.

    To use this service, you need to instantiate it with a valid Move UGC client.

    ```python
    from move_ugc import MoveUgc
    ugc = MoveUgc(api_key="my-api-key")

    # Call take service methods directly
    ugc.takes.retrieve(id="take-<guid>")

    # Or use the take service as a mixin
    take_service = ugc.takes
    take_service.retrieve(id="take-<guid>")
    ```
    """

    _schema = TakeType

    def create_singlecam(
        self,
        sources: List[SourceIn],
        name: Optional[str] = "",
        metadata: Optional[Dict[str, Any]] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> TakeType:
        """Create a singlecam take with given sources in MoveUGC.

        Args:
            sources:
                list of sources to be used for creating the take.
            name:
                name to be used for creating the take.
            metadata:
                metadata to be used for creating the take. This should be a valid json string.
            expand:
                list of fields to be expanded.
                Currently only `client` and `sources` are supported.

        Returns:
            File instance of Pydantic model type.
        """
        return self.execute(
            query_key=create_query.key,
            gql_query=create_query.generate_query(expand=expand),
            variable_values={
                "sources": [
                    source.model_dump(
                        by_alias=True,
                        exclude={"camera_settings", "clip_window"},
                    )
                    for source in sources
                ],
                "name": name,
                "metadata": self.encode_aws_metadata(metadata),
            },
        )

    def create_multicam(  # noqa: WPS211
        self,
        sources: List[SourceIn],
        volume_id: str,
        name: Optional[str] = "",
        sync_method: Optional[SyncMethodInput] = None,
        metadata: Optional[Dict[str, Any]] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> TakeType:
        """Create a multicam take with given sources in MoveUGC.

        Args:
            sources:
                list of sources to be used for creating the take.
            volume_id:
                unique identifier for the volume. This should typically be something like `volume-{uuid}`.
            name:
                name to be used for creating the take.
            sync_method:
                sync method to be used for creating the take.
            metadata:
                metadata to be used for creating the take. This should be a valid json string.
            expand:
                list of fields to be expanded.
                Currently only `client` and `sources` are supported.

        Returns:
            File instance of Pydantic model type.
        """
        sync_method_json = None
        if sync_method:
            sync_method_json = sync_method.model_dump(by_alias=True, mode="json")
        return self.execute(
            query_key=create_multicam.key,
            gql_query=create_multicam.generate_query(expand=expand),
            variable_values={
                "sources": [source.model_dump(by_alias=True) for source in sources],
                "volumeId": volume_id,
                "name": name,
                "syncMethod": sync_method_json,
                "metadata": self.encode_aws_metadata(metadata),
            },
        )

    def retrieve(
        self,
        id: str,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> TakeType:
        """Retrieve a take with given take_id from MoveUGC.

        The unique id for take will usually be in the format: `take-{uuid}`

        Args:
            id:
                unique identifier for the take. This should typically be something like `take-{uuid}`.
            expand:
                list of fields to be expanded.
                Currently only `client` and `sources` are supported.

        Returns:
            Take instance of Pydantic model type.
        """
        return self.execute(
            query_key=retrieve_query.key,
            gql_query=retrieve_query.generate_query(expand=expand),
            variable_values={"id": id},
        )

    def update(
        self,
        id: str,
        name: Optional[str] = "",
        metadata: Optional[Dict[str, Any]] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> TakeType:
        """Update a take with given take_id in MoveUGC.

        Args:
            id:
                unique identifier for the take. This should typically be something like `take-{uuid}`.
            name:
                name of the take
            metadata:
                metadata to be used for updating the take. This should be a valid json string.
            expand:
                list of fields to be expanded.
                Currently only `client` and `sources` are supported.

        Returns:
            Take instance of Pydantic model type.
        """
        encoded_metadata = None
        if metadata:
            encoded_metadata = self.encode_aws_metadata(metadata)
        return self.execute(
            query_key=update_query.key,
            gql_query=update_query.generate_query(expand=expand),
            variable_values={
                "id": id,
                "name": name,
                "metadata": encoded_metadata,
            },
        )

    def list(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        sort_by: SortDirection = SortDirection.DESC,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> ListBase:
        """List takes in MoveUGC.

        Args:
            limit:
                limit the number of items to be returned.
            next_token:
                next token to be used for pagination.
            sort_by:
                sort order for the list.
            expand:
                list of fields to be expanded.
                Currently only `client` and `sources` are supported.

        Returns:
            ListBase: List of Take instances of Pydantic model type.
        """
        if not limit:
            limit = get_default_page_size()
        return self.execute(  # type: ignore[return-value]
            query_key=list_query.key,
            gql_query=list_query.generate_query(expand=expand),
            variable_values={
                "first": limit,
                "after": next_token,
                "sortDirection": sort_by.value,
                "expand": expand,
            },
            multi=True,
        )
