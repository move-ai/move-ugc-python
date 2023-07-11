"""Queries for additional file."""
from move_ugc.gql_requests.file import expand_file

expand_additional_file = f"""
    additionalFiles {{
        key
        {expand_file}
        __typename
    }}
"""

expand_outputs = f"""
    outputs {{
        key
        {expand_file}
        __typename
    }}
"""
