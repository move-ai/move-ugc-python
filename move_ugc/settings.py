"""Global settings to be used by the SDK."""
from functools import lru_cache

from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Global settings to be used by the SDK."""

    ugc_endpoint_url: HttpUrl = Field(
        default="https://api.move.ai/ugc/graphql",
        description="Move UGC API endpoint URL",
        title="GraphQL endpoint URL",
    )
    default_page_size: int = Field(
        default=10,
        description="Default page size to be used for pagination.",
        title="Default page size",
    )
    model_config = SettingsConfigDict(env_prefix="move_")


@lru_cache(maxsize=None)
def get_settings() -> Settings:
    """Get the global settings.

    Returns:
        Settings: Global settings.
    """
    return Settings()
