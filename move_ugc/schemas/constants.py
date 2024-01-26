"""Constant values for the client."""
from typing import Literal

AUTHORIZATION_HEADER = "authorization"
MINIMUM_API_KEY_LENGTH = 12
ALLOWED_EXPAND_ATTRS = Literal[
    "client",
    "video_file",
    "additional_files",
    "outputs",
    "take",
]
CLIENT_LITERAL = "client"
TAKE_LITERAL = "take"
OUTPUTS_LITERAL = "outputs"
VIDEO_FILE_LITERAL = "video_file"
ADDITIONAL_FILE_LITERAL = "additional_files"
