"""File mixin for the Move UGC SDK."""
from typing import Any, Dict, List, Optional

from move_ugc.gql_requests.file import create as create_query
from move_ugc.gql_requests.file import generate_share_code
from move_ugc.gql_requests.file import retrieve as retrieve_query
from move_ugc.gql_requests.file import update as update_query
from move_ugc.schemas.constants import ALLOWED_EXPAND_ATTRS
from move_ugc.schemas.file import FileType, ShareCode
from move_ugc.services.base import BaseService


class FileService(BaseService[FileType]):
    """Service which can be used to communicate with File type in UGC API.

    To use this service, you need to instantiate it with a valid Move UGC client.

    ```python
    from move_ugc import MoveUgc
    ugc = MoveUgc(api_key="my-api-key")

    # Call file service methods directly
    ugc.files.retrieve(id="file-<guid>")

    # Or use the file service as a mixin
    file_service = ugc.files
    file_service.retrieve(id="file-<guid>")
    ```
    """

    _schema = FileType

    def retrieve(
        self,
        id: str,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> FileType:
        """Retrieve a file with given file_id from MoveUGC.

        The unique id for file will usually be in the format: `file-{uuid}`

        Args:
            id: unique identifier for the file. This should typically be something like `file-{uuid}`.
            expand: list of fields to be expanded. Currently only `client` is supported.

        Returns:
            File instance of Pydantic model type.
        """
        return self.execute(
            query_key=retrieve_query.key,
            gql_query=retrieve_query.generate_query(expand=expand),
            variable_values={"id": id},
        )

    def create(
        self,
        file_type: str,
        name: Optional[str] = "",
        metadata: Optional[Dict[str, Any]] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> FileType:
        """Create a file with given file type in MoveUGC.

        Args:
            file_type: type of file to be created. Example: `mp4`, `avi`, `move` etc.
            name: name of the file.
            expand: list of fields to be expanded. Currently only `client` is supported.
            metadata: metadata to be associated with the file.

        Returns:
            File instance of Pydantic model type.
        """
        return self.execute(
            query_key=create_query.key,
            gql_query=create_query.generate_query(expand=expand),
            variable_values={
                "type": file_type,
                "metadata": self.encode_aws_metadata(metadata),
                "name": name,
            },
        )

    def update(
        self,
        id: str,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> FileType:
        """Update a file with given id in MoveUGC.

        Args:
            id: unique identifier for the file. This should typically be something like `file-{uuid}`.
            expand: list of fields to be expanded. Currently only `client` is supported.
            metadata: metadata to be associated with the file.
            name: name of the file.

        Returns:
            File instance of Pydantic model type.
        """
        encoded_metadata = None
        if metadata:
            encoded_metadata = self.encode_aws_metadata(metadata)
        return self.execute(
            query_key=update_query.key,
            gql_query=update_query.generate_query(expand=expand),
            variable_values={
                "id": id,
                "metadata": encoded_metadata,
                "name": name,
            },
        )

    def generate_share_code(self, file_id: str) -> ShareCode:
        """Generate a share code with given file_id.

        Args:
            file_id:
                unique identifier for the file. This should typically be like `file-{uuid}`.

        Returns:
            ShareCode instance of Pydantic model type.
        """
        response = self.ugc_api.execute(
            generate_share_code.generate_query(),
            variable_values={"fileId": file_id},
        )
        return ShareCode(**response[generate_share_code.key])
