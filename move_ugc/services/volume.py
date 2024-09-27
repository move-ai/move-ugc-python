"""Volume service for Move UGC SDK."""
from typing import Any, Dict, List, Optional

from move_ugc.gql_requests.volume import create as create_query
from move_ugc.gql_requests.volume import retrieve_human_volume
from move_ugc.schemas.constants import ALLOWED_EXPAND_ATTRS
from move_ugc.schemas.sources import SourceIn
from move_ugc.schemas.sync_method import SyncMethodInput
from move_ugc.schemas.volume import AreaType, HumanVolumeType
from move_ugc.services.base import BaseService


class VolumeService(BaseService[HumanVolumeType]):
    """Service which can be used to communicate with Volume type in UGC API.

    To use this service, you need to instantiate it with a valid Move UGC client.

    ```python
    from move_ugc import MoveUgc
    ugc = MoveUgc(api_key="my-api-key")

    # Call volume service methods directly
    ugc.volumes.retrieve(id="volume-<guid>")

    # Or use the volume service as a mixin
    volume_service = ugc.volumes
    volume_service.retrieve(id="volume-<guid>")
    ```
    """

    _schema = HumanVolumeType

    def create_human_volume(  # noqa: WPS211
        self,
        sources: List[SourceIn],
        human_height: float,
        area_type: AreaType,
        sync_method: Optional[SyncMethodInput] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> HumanVolumeType:
        """Create a human volume with given sources in MoveUGC.

        Args:
            sources:
                list of sources to be used for creating the volume.
            human_height:
                height of the human in the volume.
            area_type:
                area type of the volume.
            sync_method:
                sync method to be used for creating the volume.
            metadata:
                metadata to be used for creating the volume. This should be a valid json string.
            name:
                name of the volume.
            expand:
                list of fields to be expanded.
                Currently only `client` and `sources` are supported.

        Returns:
            Volume instance of Pydantic model type.
        """
        return self.execute(
            query_key=create_query.key,
            gql_query=create_query.generate_query(expand=expand),
            variable_values={
                "sources": [source.model_dump(by_alias=True) for source in sources],
                "humanHeight": human_height,
                "areaType": area_type.value,
                "syncMethod": sync_method.model_dump(by_alias=True)
                if sync_method
                else None,
                "metadata": self.encode_aws_metadata(metadata),
                "name": name or "",
            },
        )

    def retrieve_human_volume(
        self,
        id: str,  # noqa: WPS125
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> HumanVolumeType:
        """Retrieve a human volume with given id from MoveUGC.

        The unique id for volume will usually be in the format: `volume-{uuid}`

        Args:
            id:
                unique identifier for the volume. This should typically be something like `volume-{uuid}`.
            expand:
                list of fields to be expanded.
                Currently only `client` and `sources` are supported.

        Returns:
            HumanVolumeType instance of Pydantic model type.
        """
        return self.execute(
            query_key=retrieve_human_volume.key,
            gql_query=retrieve_human_volume.generate_query(expand=expand),
            variable_values={"id": id},
        )
