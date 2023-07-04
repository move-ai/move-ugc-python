"""File mixin for the Move UGC SDK."""
from typing import List, Literal, Optional

from move_ugc.queries.files import retrieve as retrieve_query
from move_ugc.schemas.file import File
from move_ugc.services.base import BaseService

Expand = List[Literal["client"]]


class FileService(BaseService[File]):
    """File mixin for the Move UGC SDK."""

    _schema = File

    def retrieve(
        self,
        id: str,  # noqa: WPS125
        expand: Optional[Expand] = None,
    ) -> File:
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
