"""File queries for Move UGC API."""
from move_ugc.queries.client import expand_client_query
from move_ugc.schemas.gql import UgcGql

retrieve = UgcGql(
    query="""
    query retrieve($id: ID!){{
        getFile(fileId: $id){{
            id
            presignedUrl
            created
            type
            metadata
            {expand}
        }}
    }}
    """,
    key="getFile",
    expand={"client": expand_client_query},
)
