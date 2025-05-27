"""Constant values for the client."""

from typing import Literal

AUTHORIZATION_HEADER = "authorization"
MINIMUM_API_KEY_LENGTH = 12
ALLOWED_EXPAND_ATTRS = Literal[
    "client",
    "outputs",
    "take",
    "sources",
    "volume",
    "rig",
    "progress",
    "clipWindow",
]
CLIENT_LITERAL = "client"
TAKE_LITERAL = "take"
OUTPUTS_LITERAL = "outputs"
INPUTS_LITERAL = "inputs"
SOURCES_LITERAL = "sources"
VOLUME_LITERAL = "volume"
RIGS_LITERAL = "rig"
