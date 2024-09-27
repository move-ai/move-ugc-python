"""Graphql fragments for reusing in queries and mutations."""

human_volume_fragment = """
    fragment HumanVolumeFragment on HumanVolume {{
        id
        areaType
        created
        humanHeight
        metadata
        name
        state
        __typename
    }}
"""
