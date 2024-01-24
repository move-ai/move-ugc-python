"""Take gql requests for Move UGC SDK."""
from move_ugc.gql_requests.additional_file import expand_additional_file
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.gql_requests.file import expand_video_file
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
        "client": expand_client_query,
        "video_file": expand_video_file,
        "additional_files": expand_additional_file,
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
        "client": expand_client_query,
        "video_file": expand_video_file,
        "additional_files": expand_additional_file,
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
        "client": expand_client_query,
        "video_file": expand_video_file,
        "additional_files": expand_additional_file,
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
