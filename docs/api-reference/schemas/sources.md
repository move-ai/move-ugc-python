# Sources

::: move_ugc.schemas.sources.TakeSourceKey
    options:
        members:
            - mp4
            - avi
            - mov
            - move

::: move_ugc.schemas.sources.CameraSettings
    options:
        members:
            - lens

::: move_ugc.schemas.sources.ClipWindow
    options:
        members:
            - start_time
            - end_time

::: move_ugc.schemas.sources.AdditionalFileType
    options:
        members:
            - key
            - file


::: move_ugc.schemas.sources.SourceIn
    options:
        members:
            - device_label
            - file_id
            - format
            - camera_settings
            - clip_window

::: move_ugc.schemas.sources.Source
    options:
        members:
            - device_label
            - file
            - format
            - camera_settings
            - clip_window