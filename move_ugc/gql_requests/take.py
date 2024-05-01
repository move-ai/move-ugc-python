"""Take gql requests for Move UGC SDK."""
from move_ugc.gql_requests.additional_file import expand_additional_file
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.gql_requests.file import expand_video_file
from move_ugc.schemas.constants import (
    ADDITIONAL_FILE_LITERAL,
    CLIENT_LITERAL,
    VIDEO_FILE_LITERAL,
)
from move_ugc.schemas.gql import UgcGql

take_attributes = """
    id
    created
    metadata
    {expand}
    __typename
"""

create = UgcGql(
    query=f"""
    mutation create($video_file_id: String!, $additional_file_ids: [TakeFileInput!], $metadata: AWSJSON) {{{{
        createTake(videoFileId: $video_file_id, additionalFileIds: $additional_file_ids, metadata: $metadata) {{{{
            {take_attributes}
        }}}}
    }}}}
    """,
    key="createTake",
    expand={
        CLIENT_LITERAL: expand_client_query,
        VIDEO_FILE_LITERAL: expand_video_file,
        ADDITIONAL_FILE_LITERAL: expand_additional_file,
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
        VIDEO_FILE_LITERAL: expand_video_file,
        ADDITIONAL_FILE_LITERAL: expand_additional_file,
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
        VIDEO_FILE_LITERAL: expand_video_file,
        ADDITIONAL_FILE_LITERAL: expand_additional_file,
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
        VIDEO_FILE_LITERAL: expand_video_file,
        ADDITIONAL_FILE_LITERAL: expand_additional_file,
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
