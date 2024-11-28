"""Camera settings gql requests for Move UGC SDK."""

from move_ugc.gql_requests.file import expand_video_file
from move_ugc.schemas.gql import UgcGql

camera_settings_attributes = """
    lens
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

list_query = UgcGql(
    query=f"""
    query list {{{{
        listCameraSettings {{{{
            items {{{{
                {camera_settings_attributes}
            }}}}
        }}}}
    }}}}
    """,
    key="listCameraSettings",
)
