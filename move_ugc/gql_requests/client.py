"""Queries for client."""
from move_ugc.schemas.gql import UgcGql

client_attributes_base = """
    id
    name
    created
    metadata
    portal
    __typename
"""

expand_client_query = f"""
    client {{
        {client_attributes_base}
    }}
"""

retrieve = UgcGql(
    query=f"""
    query retrieve {{{{
        client {{{{
            {client_attributes_base}
        }}}}
    }}}}
    """,
    key="client",
)


update = UgcGql(
    query=f"""
    mutation update($metadata: AWSJSON!) {{{{
        updateClient (metadata: $metadata) {{{{
            {client_attributes_base}
        }}}}
    }}}}
    """,
    key="updateClient",
)
