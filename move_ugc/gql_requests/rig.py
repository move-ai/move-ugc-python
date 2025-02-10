"""Queries for rig."""
from move_ugc.schemas.gql import UgcGql

rig_attributes_base = """
    name
    __typename
"""

expand_rig_query = f"""
    rig {{
        {rig_attributes_base}
    }}
"""

list_query = UgcGql(
    query=f"""
    query list {{{{
        listRigs {{{{
            items {{{{
                {rig_attributes_base}
            }}}}
        }}}}
    }}}}
    """,
    key="listRigs",
)
