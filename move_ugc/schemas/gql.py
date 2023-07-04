"""GraphQL helper schemas."""
from typing import Dict, List, Optional

from gql import gql
from graphql import DocumentNode
from pydantic import BaseModel

from move_ugc.schemas.constants import ALLOWED_EXPAND_ATTRS


class UgcGql(BaseModel):
    """GraphQL query."""

    query: str
    key: str
    expand: Dict[str, str]

    def generate_query(
        self,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> DocumentNode:
        """Get the query with the expanded fields.

        Args:
            expand: List of fields to be expanded.

        Returns:
            DocumentNode: Query with the expanded fields.
        """
        expand_query = ""
        if expand:
            expand_query = "\n".join(
                [self.expand[field] for field in expand],
            )
        return gql(self.query.format(expand=expand_query))
