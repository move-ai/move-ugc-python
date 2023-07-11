"""Take service for Move UGC SDK."""
from typing import List, Optional

from move_ugc.gql_requests.job import create as create_query
from move_ugc.gql_requests.job import retrieve as retrieve_query
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
