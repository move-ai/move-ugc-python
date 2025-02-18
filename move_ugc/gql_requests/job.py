"""Job gql requests for Move UGC SDK."""

from move_ugc.gql_requests.additional_file import expand_outputs
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.gql_requests.rig import expand_rig_query
from move_ugc.gql_requests.take import expand_take_query
from move_ugc.schemas.constants import (
    CLIENT_LITERAL,
    OUTPUTS_LITERAL,
    RIGS_LITERAL,
    TAKE_LITERAL,
)
from move_ugc.schemas.gql import UgcGql

job_attributes = """
    id
    created
    metadata
    state
    name
    {expand}
    __typename
"""

create = UgcGql(
    query=f"""
    mutation create(
        $take_id: String!,
        $name: String,
        $options: OptionsInput,
        $outputs: [OutputType],
        $metadata: AWSJSON,
        $clip_window: ClipWindowInput
    ) {{{{
        createSingleCamJob(
            takeId: $take_id,
            name: $name,
            options: $options,
            outputs: $outputs,
            metadata: $metadata
            clipWindow: $clip_window
        ) {{{{
            {job_attributes}
        }}}}
    }}}}
    """,
    key="createSingleCamJob",
    expand={
        CLIENT_LITERAL: expand_client_query,
        TAKE_LITERAL: expand_take_query,
        OUTPUTS_LITERAL: expand_outputs,
    },
)

create_multicam = UgcGql(
    query=f"""
    mutation create(
        $take_id: String!,
        $name: String,
        $numberOfActors: Int!,
        $options: OptionsInput,
        $outputs: [OutputType],
        $metadata: AWSJSON,
        $rig: String,
        $clip_window: ClipWindowInput,
    ) {{{{
        createMultiCamJob(
            takeId: $take_id,
            name: $name,
            numberOfActors: $numberOfActors,
            options: $options,
            outputs: $outputs,
            metadata: $metadata
            rig: $rig
            clipWindow: $clip_window
        ) {{{{
            {job_attributes}
        }}}}
    }}}}
    """,
    key="createMultiCamJob",
    expand={
        CLIENT_LITERAL: expand_client_query,
        TAKE_LITERAL: expand_take_query,
        OUTPUTS_LITERAL: expand_outputs,
        RIGS_LITERAL: expand_rig_query,
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
        RIGS_LITERAL: expand_rig_query,
    },
)

update = UgcGql(
    query=f"""
    mutation update(
        $id: String!,
        $metadata: AWSJSON,
        $name: String
    ) {{{{
        updateJob(
            id: $id,
            metadata: $metadata,
            name: $name
        ) {{{{
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
        RIGS_LITERAL: expand_rig_query,
    },
)
