"""Camera setting service for move-ugc-python-sdk."""

from move_ugc.gql_requests.camera_settings import list_query
from move_ugc.schemas.commons import ListBaseItems
from move_ugc.schemas.sources import CameraSettings
from move_ugc.services.base import BaseService


class CameraSettingsService(BaseService[CameraSettings]):
    """Service which can be used to communicate with Camera settings in UGC API.

    To use this service, you need to instantiate it with a valid Move UGC client.

    python
    from move_ugc import MoveUgc
    ugc = MoveUgc(api_key="my-api-key")

    # Call camera settings service methods directly
    ugc.camera_settings.list()
    """

    _schema = CameraSettings
    _list_base_schema = ListBaseItems

    def list(  # noqa: WPS211
        self,
    ) -> ListBaseItems:
        """List Camera settings in MoveUGC.

        Returns:
            ListBaseItems: List of Camera settings instances of Pydantic model type.
        """
        return self.execute(  # type: ignore[return-value]
            query_key=list_query.key,
            gql_query=list_query.generate_query(),
            multi=True,
        )
