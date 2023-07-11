"""Job gql requests for Move UGC SDK."""
from move_ugc.gql_requests.additional_file import expand_outputs
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.gql_requests.take import expand_take_query
from move_ugc.schemas.gql import UgcGql

create = UgcGql(
    query="""
    mutation create($take_id: String!, $metadata: AWSJSON){{
        createJob(takeId: $take_id, metadata: $metadata){{
            id
            created
            metadata
            state
            {expand}
            __typename
        }}
    }}
    """,
    key="createJob",
    expand={
        "client": expand_client_query,
        "take": expand_take_query,
        "outputs": expand_outputs,
    },
)


retrieve = UgcGql(
    query="""
    query retrieve($id: ID!){{
        getJob(jobId: $id){{
            id
            created
            metadata
            state
            {expand}
            __typename
        }}
    }}
    """,
    key="getJob",
    expand={
        "client": expand_client_query,
        "take": expand_take_query,
        "outputs": expand_outputs,
    },
)
