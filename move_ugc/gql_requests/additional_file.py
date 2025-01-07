"""Queries for additional file."""

from move_ugc.gql_requests.file import expand_file

# TODO: When `key` is deprecated this should be changed to `format`
expand_outputs = f"""
    outputs {{
        key
        {expand_file}
        __typename
    }}
"""


# TODO: volumes only support `format` for outputs. When `key` is deprecated
#  this should be removed and rolled in with the above
expand_outputs_format = f"""
    outputs {{
        format
        {expand_file}
        __typename
    }}
"""
