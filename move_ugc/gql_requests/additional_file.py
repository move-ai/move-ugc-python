"""Queries for additional file."""
from move_ugc.gql_requests.file import expand_file

expand_outputs = f"""
    outputs {{
        key
        {expand_file}
        __typename
    }}
"""
