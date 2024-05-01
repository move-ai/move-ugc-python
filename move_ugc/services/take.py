"""Take service for Move UGC SDK."""
from typing import Any, Dict, List, Optional

from move_ugc.gql_requests.take import create as create_query
from move_ugc.gql_requests.take import list_query
from move_ugc.gql_requests.take import retrieve as retrieve_query
from move_ugc.gql_requests.take import update as update_query
from move_ugc.schemas.additional_file import AdditionalFileIn
from move_ugc.schemas.commons import ListBase, SortDirection, get_default_page_size
from move_ugc.schemas.constants import ALLOWED_EXPAND_ATTRS
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

    def create(
        self,
        video_file_id: str,
        additional_files: Optional[List[AdditionalFileIn]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> TakeType:
        """Create a file with given file type in MoveUGC.

        Args:
            video_file_id:
                id of the video file to be used for creating the take.
                This usually contains a video file with extensions such as `mp4`, `avi`, `mov` etc.
            metadata:
                metadata to be used for creating the take. This should be a valid json string.
            additional_files:
                list of additional files to be used for creating the take.
            expand:
                list of fields to be expanded.
                Currently only `client`, `video_file` and `additional_files` are supported.

        Returns:
            File instance of Pydantic model type.
        """
        return self.execute(
            query_key=create_query.key,
            gql_query=create_query.generate_query(expand=expand),
            variable_values={
                "video_file_id": video_file_id,
                "additional_file_ids": [
                    additional_file.model_dump(by_alias=True)
                    for additional_file in (additional_files or [])
                ],
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
                Currently only `client`, `video_file` and `additional_files` are supported.

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
        metadata: Optional[Dict[str, Any]] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> TakeType:
        """Update a take with given take_id in MoveUGC.

        Args:
            id:
                unique identifier for the take. This should typically be something like `take-{uuid}`.
            metadata:
                metadata to be used for updating the take. This should be a valid json string.
            expand:
                list of fields to be expanded.
                Currently only `client`, `video_file` and `additional_files` are supported.

        Returns:
            Take instance of Pydantic model type.
        """
        return self.execute(
            query_key=update_query.key,
            gql_query=update_query.generate_query(expand=expand),
            variable_values={
                "id": id,
                "metadata": self.encode_aws_metadata(metadata),
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
                Currently only `client`, `video_file` and `additional_files` are supported.

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
