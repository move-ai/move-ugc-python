"""Take service for Move UGC SDK."""
from typing import List, Optional

from move_ugc.gql_requests.job import create as create_query
from move_ugc.gql_requests.job import list_query
from move_ugc.gql_requests.job import retrieve as retrieve_query
from move_ugc.schemas.commons import ListBase, SortDirection, get_default_page_size
from move_ugc.schemas.constants import ALLOWED_EXPAND_ATTRS
from move_ugc.schemas.job import JobType
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
        metadata: Optional[str] = None,
        expand: Optional[List[ALLOWED_EXPAND_ATTRS]] = None,
    ) -> JobType:
        """Create a job in MoveUGC.

        Args:
            take_id:
                id of the take to be used for creating the job.
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
                "metadata": metadata,
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

    def list(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        sort_by: SortDirection = SortDirection.DESC,
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
            },
            multi=True,
        )
