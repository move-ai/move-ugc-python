"""Camera settings gql requests for Move UGC SDK."""
from move_ugc.gql_requests.file import expand_video_file

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
