"""GraphQL helper schemas."""
import copy
from typing import Dict, List, Optional

from gql import gql
from graphql import DocumentNode
from pydantic import BaseModel, Field

from move_ugc.gql_requests.fragments import human_volume_fragment
from move_ugc.schemas.constants import ALLOWED_EXPAND_ATTRS, VOLUME_LITERAL


class UgcGql(BaseModel):
    """GraphQL query."""

    query: str
    key: str
    expand: Dict[str, str] = Field(default_factory=dict)

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
        query = copy.deepcopy(self.query)
        expand_query = ""
        if expand:
            expand_query = "\n".join(
                [self.expand[field] for field in expand],
            )
            if VOLUME_LITERAL in expand:
                # Add all union type fragments
                query += "\n".join([human_volume_fragment])

        return gql(query.format(expand=expand_query))
