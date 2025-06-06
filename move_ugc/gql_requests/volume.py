"""Volume gql requests for Move UGC SDK."""

from move_ugc.gql_requests.additional_file import expand_outputs
from move_ugc.gql_requests.camera_settings import expand_sources_w_camera_settings
from move_ugc.gql_requests.client import expand_client_query
from move_ugc.gql_requests.inputs import expand_clip_window, expand_progress
from move_ugc.schemas.constants import CLIENT_LITERAL, OUTPUTS_LITERAL, SOURCES_LITERAL
from move_ugc.schemas.gql import UgcGql

human_volume_attributes = f"""
    id
    areaType
    created
    humanHeight
    metadata
    name
    state
    {expand_progress}
    {{expand}}
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
        $clip_window: ClipWindowInput,
    ) {{{{
        createVolumeWithHuman(
            sources: $sources,
            syncMethod: $syncMethod,
            areaType: $areaType,
            humanHeight: $humanHeight,
            metadata: $metadata,
            name: $name,
            clipWindow: $clip_window
        ) {{{{
            {human_volume_attributes}
        }}}}
    }}}}
    """,
    key="createVolumeWithHuman",
    expand={
        CLIENT_LITERAL: expand_client_query,
        SOURCES_LITERAL: expand_sources_w_camera_settings,
        "clipWindow": expand_clip_window,
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
        OUTPUTS_LITERAL: expand_outputs,
    },
)


expand_volume_query = """
    volume {
        ... on Volume {
            ...HumanVolumeFragment
        }
    }
"""


list_query = UgcGql(
    query=f"""
    query list($first: Int, $after: AWSJSON, $sortDirection: SortDirection) {{{{
        listVolumes(first: $first, after: $after, sortDirection: $sortDirection) {{{{
            first
            after
            items {{{{
                ... on Volume {{{{
                    ...VolumeFields
                }}}}
            }}}}
        }}}}
    }}}}
    fragment VolumeFields on HumanVolume {{{{
        {human_volume_attributes}
    }}}}
    """,
    key="listVolumes",
    expand={
        CLIENT_LITERAL: expand_client_query,
        SOURCES_LITERAL: expand_sources_w_camera_settings,
        OUTPUTS_LITERAL: expand_outputs,
    },
)
