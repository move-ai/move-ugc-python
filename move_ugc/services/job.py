"""Take service for Move UGC SDK."""
from typing import Any, Dict, List, Optional
from warnings import warn

from move_ugc.gql_requests.job import create as create_query
from move_ugc.gql_requests.job import create_multicam, list_query
from move_ugc.gql_requests.job import retrieve as retrieve_query
from move_ugc.gql_requests.job import update as update_query
from move_ugc.schemas.commons import ListBase, SortDirection, get_default_page_size
from move_ugc.schemas.constants import ALLOWED_EXPAND_ATTRS
from move_ugc.schemas.job import JobOptions, JobType
from move_ugc.services.base import BaseService


class JobService(BaseService[JobType]):
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

    _schema = JobType

    def create(
        self,
        take_id: str,
        name: Optional[str] = "",
        metadata: Optional[Dict[str, Any]] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> JobType:
        """Create a singlecam job in MoveUGC.

        Args:
            take_id:
                id of the take to be used for creating the job.
            name:
                name to be used for creating the job.
            metadata:
                metadata to be used for creating the job. This should be a valid json string.
            expand:
                list of fields to be expanded.
                Currently only `client`, `take` and `outputs` are supported.

        Returns:
            Job instance of Pydantic model type.
        """
        warn(
            "This method is deprecated. Use create_singlecam instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.create_singlecam(
            take_id=take_id,
            name=name,
            metadata=metadata,
            expand=expand,
        )

    def create_singlecam(
        self,
        take_id: str,
        name: Optional[str] = "",
        metadata: Optional[Dict[str, Any]] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> JobType:
        """Create a singlecam job in MoveUGC.

        Args:
            take_id:
                id of the take to be used for creating the job.
            name:
                name to be used for creating the job.
            metadata:
                metadata to be used for creating the job. This should be a valid json string.
            expand:
                list of fields to be expanded.
                Currently only `client`, `take` and `outputs` are supported.

        Returns:
            Job instance of Pydantic model type.
        """
        return self.execute(
            query_key=create_query.key,
            gql_query=create_query.generate_query(expand=expand),
            variable_values={
                "take_id": take_id,
                "name": name,
                "metadata": self.encode_aws_metadata(metadata),
            },
        )

    def create_multicam(  # noqa: WPS211
        self,
        take_id: str,
        number_of_actors: int,
        options: Optional[JobOptions] = None,
        name: Optional[str] = "",
        metadata: Optional[Dict[str, Any]] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> JobType:
        """Create a multicam job in MoveUGC.

        Args:
            take_id:
                id of the take to be used for creating the job.
            number_of_actors:
                number of actors to be used for creating the job.
            options:
                options to be used for creating the job.
                Check all the valid allowed options in the API documentation.
                https://move-ai.github.io/move-ugc-api/schema/#optionsinput
            name:
                name to be used for creating the job.
            metadata:
                metadata to be used for creating the job. This should be a valid json string.
            expand:
                list of fields to be expanded.
                Currently only `client`, `take` and `outputs` are supported.

        Returns:
            Job instance of Pydantic model type.
        """
        options = options or JobOptions()
        return self.execute(
            query_key=create_multicam.key,
            gql_query=create_multicam.generate_query(expand=expand),
            variable_values={
                "take_id": take_id,
                "numberOfActors": number_of_actors,
                "name": name,
                "options": options.model_dump(by_alias=True, mode="json"),
                "metadata": self.encode_aws_metadata(metadata),
            },
        )

    def retrieve(
        self,
        id: str,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> JobType:
        """Retrieve a job from MoveUGC.

        Args:
            id:
                id of the job to be retrieved.
            expand:
                list of fields to be expanded.
                Currently only `client`, `take` and `outputs` are supported.

        Returns:
            Job instance of Pydantic model type.
        """
        return self.execute(
            query_key=retrieve_query.key,
            gql_query=retrieve_query.generate_query(expand=expand),
            variable_values={"id": id},
        )

    def update(
        self,
        id: str,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> JobType:
        """Update a job with given job in MoveUGC.

        Args:
            id:
                unique identifier for the take. This should typically be something like `take-{uuid}`.
            metadata:
                metadata to be used for updating the take. This should be a valid json string.
            name:
                name to be used for updating the take.
            expand:
                list of fields to be expanded.
                Currently only `client`, `output`, `take` and `sources` are supported.

        Returns:
            Take instance of Pydantic model type.
        """
        encoded_metadata = None
        if metadata:
            encoded_metadata = self.encode_aws_metadata(metadata)
        return self.execute(
            query_key=update_query.key,
            gql_query=update_query.generate_query(expand=expand),
            variable_values={
                "id": id,
                "metadata": encoded_metadata,
                "name": name,
            },
        )

    def list(  # noqa: WPS211
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        sort_by: SortDirection = SortDirection.DESC,
        take_id: Optional[str] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> ListBase:
        """List jobs in MoveUGC.

        Args:
            limit:
                limit the number of items to be returned.
            next_token:
                next token to be used for pagination.
            sort_by:
                sort order for the list.
            take_id:
                id of the take to be used for filtering the jobs.
            expand:
                list of fields to be expanded.
                Currently only `client`, `take` and `outputs` are supported.

        Returns:
            ListBase: List of Job instances of Pydantic model type.
        """
        if not limit:
            limit = get_default_page_size()
        return self.execute(  # type: ignore[return-value]
            query_key=list_query.key,
            gql_query=list_query.generate_query(expand=expand),
            variable_values={
                "first": limit,
                "after": next_token,
                "sortDirection": sort_by.value,
                "expand": expand,
                "takeId": take_id,
            },
            multi=True,
        )
