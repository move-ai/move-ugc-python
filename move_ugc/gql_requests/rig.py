"""Queries for rig."""

rig_attributes_base = """
    name
    __typename
"""

expand_rig_query = f"""
    rig {{
        {rig_attributes_base}
    }}
"""
