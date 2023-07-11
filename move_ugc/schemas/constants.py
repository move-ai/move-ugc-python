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
