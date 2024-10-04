"""File gql_requests for Move UGC API."""
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.schemas.gql import UgcGql

expand_file_base = """
    id
    created
    type
    metadata
    name
    presignedUrl
    thumbnailUrl
    __typename
"""

file_attributes = f"""
    {expand_file_base}
    {{expand}}
"""


retrieve = UgcGql(
    query=f"""
    query retrieve($id: ID!) {{{{
        getFile(fileId: $id) {{{{
            {file_attributes}
        }}}}
    }}}}
    """,
    key="getFile",
    expand={"client": expand_client_query},
)


create = UgcGql(
    query=f"""
    mutation create(
        $type: String!,
        $metadata: AWSJSON,
        $name: String
    ) {{{{
        createFile(
            type: $type,
            metadata: $metadata,
            name: $name
        ) {{{{
            {file_attributes}
        }}}}
    }}}}
    """,
    key="createFile",
    expand={"client": expand_client_query},
)

update = UgcGql(
    query=f"""
    mutation update(
        $id: String!,
        $metadata: AWSJSON,
        $name: String
    ) {{{{
        updateFile(
            id: $id,
            metadata: $metadata,
            name: $name
        ) {{{{
            {file_attributes}
        }}}}
    }}}}
    """,
    key="updateFile",
    expand={"client": expand_client_query},
)


generate_share_code = UgcGql(
    query="""
    mutation generateShareCode($fileId: String!) {{
        generateShareCode(fileId: $fileId) {{
            code
            created
            file {{
                id
            }}
            expires
            url
            __typename
        }}
    }}
    """,
    key="generateShareCode",
)

expand_video_file = f"""
    file {{
        {expand_file_base}
    }}
"""

expand_file = f"""
    file {{
        {expand_file_base}
    }}
"""
