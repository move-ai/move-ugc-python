"""Take gql requests for Move UGC SDK."""
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.gql_requests.file import expand_video_file
from move_ugc.schemas.constants import CLIENT_LITERAL, SOURCES_LITERAL
from move_ugc.schemas.gql import UgcGql

take_attributes = """
    id
    created
    metadata
    {expand}
    __typename
"""

expand_sources = f"""
    sources {{
        deviceLabel
        {expand_video_file}
        format
    }}
"""

create = UgcGql(
    query=f"""
    mutation create($sources: [SourceInput!], $metadata: AWSJSON) {{{{
        createSingleCamTake(sources: $sources, metadata: $metadata) {{{{
            {take_attributes}
        }}}}
    }}}}
    """,
    key="createSingleCamTake",
    expand={
        CLIENT_LITERAL: expand_client_query,
        SOURCES_LITERAL: expand_sources,
    },
)


retrieve = UgcGql(
    query=f"""
    query retrieve($id: ID!) {{{{
        getTake(takeId: $id) {{{{
            {take_attributes}
        }}}}
    }}}}
    """,
    key="getTake",
    expand={
        CLIENT_LITERAL: expand_client_query,
        SOURCES_LITERAL: expand_sources,
    },
)

update = UgcGql(
    query=f"""
    mutation update($id: String!, $metadata: AWSJSON!) {{{{
        updateTake(id: $id, metadata: $metadata) {{{{
            {take_attributes}
        }}}}
    }}}}
    """,
    key="updateTake",
    expand={
        CLIENT_LITERAL: expand_client_query,
        SOURCES_LITERAL: expand_sources,
    },
)

list_query = UgcGql(
    query=f"""
    query list($first: Int, $after: AWSJSON, $sortDirection: SortDirection) {{{{
        listTakes(first: $first, after: $after, sortDirection: $sortDirection) {{{{
            first
            after
            items {{{{
                {take_attributes}
            }}}}
        }}}}
    }}}}
    """,
    key="listTakes",
    expand={
        CLIENT_LITERAL: expand_client_query,
        SOURCES_LITERAL: expand_sources,
    },
)


expand_take_query = """
    take {
        id
        created
        metadata
        __typename
    }
"""
