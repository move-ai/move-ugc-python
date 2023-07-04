"""Move UGC SDK client."""
from move_ugc.schemas.metaclient import MetaClient
from move_ugc.services.files import FileService


class MoveUgc(MetaClient):
    """Move UGC SDK client."""

    @property
    def files(self) -> FileService:
        """Get the file mixin.

        Returns:
            FileService: The file mixin.
        """
        return FileService(**self.model_dump())
