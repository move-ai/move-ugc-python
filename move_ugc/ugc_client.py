"""Move UGC SDK client."""
from move_ugc.schemas.metaclient import MetaClient
from move_ugc.services.client import ClientService
from move_ugc.services.file import FileService
from move_ugc.services.job import JobService
from move_ugc.services.take import TakeService
from move_ugc.services.volume import VolumeService
from move_ugc.services.webhooks import WebhookService


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

    @property
    def client(self) -> ClientService:
        """Get the client service.

        Returns:
            ClientService: The client service.
        """
        return ClientService(**self.model_dump())

    @property
    def webhooks(self) -> WebhookService:
        """Get the webhook service.

        Returns:
            WebhookService: The webhook service.
        """
        return WebhookService(**self.model_dump())

    @property
    def volumes(self) -> VolumeService:
        """Get the volume service.

        Returns:
            VolumeService: The volume service.
        """
        return VolumeService(**self.model_dump())
