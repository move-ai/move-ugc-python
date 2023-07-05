"""File gql_requests for Move UGC API."""
from move_ugc.gql_requests.client import expand_client_query
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
            __typename
        }}
    }}
    """,
    key="getFile",
    expand={"client": expand_client_query},
)


create = UgcGql(
    query="""
    mutation create($type: String!){{
        createFile(type: $type){{
            id
            presignedUrl
            created
            type
            metadata
            {expand}
            __typename
        }}
    }}
    """,
    key="createFile",
    expand={"client": expand_client_query},
)
