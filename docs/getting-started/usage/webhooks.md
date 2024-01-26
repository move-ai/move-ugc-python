UGC API can easily be integrated with custom webhooks to get updates when an event is triggered by us. To create a webhook, you need to specify the URL of your webhook, a secret and the events you want to receive updates for.

Currently, the available events can be found at this link. You can subscribe to any of these events using either the hosted portal url fetched as part of `ugc.client.retrieve` or `ugc.webhooks.upsert` method directly.


## Subscribing to events

```python
events = ["ugc.job.state.completed", "ugc.job.state.failed"]
uid = "my-webhook"
url = "https://my-webhook.com"

webhook = ugc.webhooks.upsert(uid=uid, url=url, events=events)
```

Please note that `secret` will only be returned when you create the webhook for the first time through `.secret`. You cannot update a secret of an existing webhook.
To see the secret again, you can use `ugc.client.retrieve` method and go to the portal url.

