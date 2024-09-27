"""Volume gql requests for Move UGC SDK."""
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.gql_requests.file import expand_video_file
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

expand_camera_settings = """
    cameraSettings {
        lens
    }
"""

expand_sources_w_camera_settings = f"""
    sources {{
        deviceLabel
        {expand_video_file}
        {expand_camera_settings}
        format
    }}
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
        SOURCES_LITERAL: expand_sources_w_camera_settings,
    },
)


retrieve_human_volume = UgcGql(
    query=f"""
    query retrieve($id: ID!) {{{{
        getVolume(id: $id) {{{{
                ... on Volume {{{{
                ...VolumeFields
            }}}}
        }}}}
    }}}}
    fragment VolumeFields on HumanVolume {{{{
        {human_volume_attributes}
    }}}}
    """,
    key="getVolume",
    expand={
        CLIENT_LITERAL: expand_client_query,
        SOURCES_LITERAL: expand_sources_w_camera_settings,
    },
)


expand_volume_query = """
    volume {
        ... on Volume {
            ...HumanVolumeFragment
        }
    }
"""
