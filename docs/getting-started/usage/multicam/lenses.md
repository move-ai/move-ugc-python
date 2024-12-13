# Camera lenses

The multicam methods requires you to specify the type of camera that the video inputs where shot on. Only certain lenses are supported. You can find this list by making a query with [this](/move-ugc-python/latest/api-reference/services/camera_settings/#move_ugc.services.camera_settings.CameraSettingsService.list) method.

```python
lenses = ugc.camera_settings.list()
```