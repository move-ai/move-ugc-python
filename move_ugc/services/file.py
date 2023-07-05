"""File mixin for the Move UGC SDK."""
from typing import List, Literal, Optional

from move_ugc.gql_requests.file import create as create_query
from move_ugc.gql_requests.file import retrieve as retrieve_query
from move_ugc.schemas.file import FileType
from move_ugc.services.base import BaseService

Expand = List[Literal["client"]]


class FileService(BaseService[FileType]):
    """File mixin for the Move UGC SDK."""

    _schema = FileType

    def retrieve(
        self,
        id: str,  # noqa: WPS125
        expand: Optional[Expand] = None,
    ) -> FileType:
        """Retrieve a file from UGC API.

        Args:
            id: unique identifier for the file. This should typically be something like `file-<guid>`.
            expand: list of fields to be expanded. Currently only `client` is supported.

        Returns:
            File instance of Pydantic model type.
        """
        return self.execute(
            query_key=retrieve_query.key,
            gql_query=retrieve_query.generate_query(expand=expand or []),
            variable_values={"id": id},
        )

    def create(self, file_type: str, expand: Optional[Expand] = None) -> FileType:
        """Create a file from UGC API.

        Args:
            file_type: type of file to be created.
            expand: list of fields to be expanded. Currently only `client` is supported.

        Returns:
            File instance of Pydantic model type.
        """
        return self.execute(
            query_key=create_query.key,
            gql_query=create_query.generate_query(expand=expand or []),
            variable_values={"type": file_type},
        )
