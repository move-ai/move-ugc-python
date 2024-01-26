"""Job gql requests for Move UGC SDK."""
from move_ugc.gql_requests.additional_file import expand_outputs
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.gql_requests.take import expand_take_query
from move_ugc.schemas.constants import CLIENT_LITERAL, OUTPUTS_LITERAL, TAKE_LITERAL
from move_ugc.schemas.gql import UgcGql

job_attributes = """
    id
    created
    metadata
    state
    {expand}
    __typename
"""

create = UgcGql(
    query=f"""
    mutation create($take_id: String!, $metadata: AWSJSON) {{{{
        createJob(takeId: $take_id, metadata: $metadata) {{{{
            {job_attributes}
        }}}}
    }}}}
    """,
    key="createJob",
    expand={
        CLIENT_LITERAL: expand_client_query,
        TAKE_LITERAL: expand_take_query,
        OUTPUTS_LITERAL: expand_outputs,
    },
)


retrieve = UgcGql(
    query=f"""
    query retrieve($id: ID!) {{{{
        getJob(jobId: $id) {{{{
            {job_attributes}
        }}}}
    }}}}
    """,
    key="getJob",
    expand={
        CLIENT_LITERAL: expand_client_query,
        TAKE_LITERAL: expand_take_query,
        OUTPUTS_LITERAL: expand_outputs,
    },
)

update = UgcGql(
    query=f"""
    mutation update($id: String!, $metadata: AWSJSON!) {{{{
        updateJob(id: $id, metadata: $metadata) {{{{
            {job_attributes}
        }}}}
    }}}}
    """,
    key="updateJob",
    expand={
        CLIENT_LITERAL: expand_client_query,
        TAKE_LITERAL: expand_take_query,
        OUTPUTS_LITERAL: expand_outputs,
    },
)

list_query = UgcGql(
    query=f"""
    query list($first: Int, $after: AWSJSON, $sortDirection: SortDirection, $takeId: String) {{{{
        listJobs(first: $first, after: $after, sortDirection: $sortDirection, takeId: $takeId) {{{{
            first
            after
            items {{{{
                {job_attributes}
            }}}}
        }}}}
    }}}}
    """,
    key="listJobs",
    expand={
        CLIENT_LITERAL: expand_client_query,
        TAKE_LITERAL: expand_take_query,
        OUTPUTS_LITERAL: expand_outputs,
    },
)
