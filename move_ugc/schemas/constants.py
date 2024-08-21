"""Constant values for the client."""
from typing import Literal

AUTHORIZATION_HEADER = "authorization"
MINIMUM_API_KEY_LENGTH = 12
ALLOWED_EXPAND_ATTRS = Literal[
    "client",
    "outputs",
    "take",
    "sources",
]
CLIENT_LITERAL = "client"
TAKE_LITERAL = "take"
OUTPUTS_LITERAL = "outputs"
SOURCES_LITERAL = "sources"
