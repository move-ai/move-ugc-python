"""Take gql requests for Move UGC SDK."""
from move_ugc.schemas.gql import UgcGql

add_webhook = UgcGql(
    query="""
    mutation addWebhook($events: [String!]!, $uid: String!, $url: String!, $description: String, $secret: String) {{
        upsertWebhookEndpoint(events: $events, uid: $uid, url: $url, description: $description, secret: $secret) {{
            description
            events
            uid
            url
            secret
        }}
    }}
    """,
    key="upsertWebhookEndpoint",
)
