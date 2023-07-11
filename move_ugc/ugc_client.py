"""Move UGC SDK client."""
from move_ugc.schemas.metaclient import MetaClient
from move_ugc.services.file import FileService
from move_ugc.services.job import JobService
from move_ugc.services.take import TakeService


class MoveUgc(MetaClient):
    """Move UGC SDK client."""

    @property
    def files(self) -> FileService:
        """Get the file service.

        Returns:
            FileService: The file service.
        """
        return FileService(**self.model_dump())

    @property
    def takes(self) -> TakeService:
        """Get the take service.

        Returns:
            TakeService: The take service.
        """
        return TakeService(**self.model_dump())

    @property
    def jobs(self) -> JobService:
        """Get the job service.

        Returns:
            JobService: The job service.
        """
        return JobService(**self.model_dump())
