"""Take service for Move UGC SDK."""
from typing import List, Optional

from move_ugc.gql_requests.take import create as create_query
from move_ugc.gql_requests.take import retrieve as retrieve_query
from move_ugc.schemas.additional_file import AdditionalFileIn
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
        metadata: Optional[str] = None,
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
                "metadata": metadata or "null",
            },
        )

    def retrieve(
        self,
        id: str,  # noqa: WPS125
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
