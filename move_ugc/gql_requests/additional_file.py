"""Queries for additional file."""

from move_ugc.gql_requests.file import expand_file

# TODO: When `key` is deprecated this should be changed to `format`
expand_outputs = f"""
    outputs {{
        format
        {expand_file}
        __typename
    }}
"""
