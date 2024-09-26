"""Volume gql requests for Move UGC SDK."""
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.gql_requests.take import expand_sources
from move_ugc.schemas.constants import CLIENT_LITERAL, SOURCES_LITERAL
from move_ugc.schemas.gql import UgcGql

human_volume_attributes = """
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    {expand}
    __typename
"""

create = UgcGql(
    query=f"""
    mutation create(
        $sources: [SourceInput!],
        $syncMethod: SyncMethodInput,
        $areaType: AreaType!,
        $humanHeight: Float!,
        $metadata: AWSJSON,
        $name: String,
    ) {{{{
        createVolumeWithHuman(
            sources: $sources,
            syncMethod: $syncMethod,
            areaType: $areaType,
            humanHeight: $humanHeight,
            metadata: $metadata,
            name: $name,
        ) {{{{
            {human_volume_attributes}
        }}}}
    }}}}
    """,
    key="createVolumeWithHuman",
    expand={
        CLIENT_LITERAL: expand_client_query,
        SOURCES_LITERAL: expand_sources,
    },
)
