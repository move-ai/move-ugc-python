"""Camera setting service for move-ugc-python-sdk."""
from typing import Any, Dict, List, Optional
from warnings import warn

from move_ugc.gql_requests.camera_settings import list_query
from move_ugc.schemas.commons import ListBase, SortDirection, get_default_page_size
from move_ugc.schemas.constants import ALLOWED_EXPAND_ATTRS
from move_ugc.schemas.sources import CameraSettings
from move_ugc.services.base import BaseService

class CameraSettingsService(BaseService[CameraSettings]):
    """Service which can be used to communicate with Job type in UGC API.

    To use this service, you need to instantiate it with a valid Move UGC client.

    ```python
    from move_ugc import MoveUgc
    ugc = MoveUgc(api_key="my-api-key")

    # Call job service methods directly
    ugc.jobs.retrieve(id="job-<guid>")

    # Or use the job service as a mixin
    job_service = ugc.jobs
    job_service.retrieve(id="job-<guid>")
    ```
    """

    _schema = CameraSettings


    def list(  # noqa: WPS211
        self,
    ) -> ListBase:
        """List jobs in MoveUGC.

        Returns:
            ListBase: List of Job instances of Pydantic model type.
        """

        return self.execute(  # type: ignore[return-value]
            query_key=list_query.key,
            gql_query=list_query.generate_query(),
            multi=True,
        )
