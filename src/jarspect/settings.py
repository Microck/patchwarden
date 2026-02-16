from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "Jarspect"
    service_version: str = "0.1.0"
    app_env: str = "dev"
    log_level: str = "INFO"
    storage_backend: str = "local"
    local_storage_dir: str = ".local-data/uploads"
    upload_max_bytes: int = 50 * 1024 * 1024

    azure_storage_connection_string: str | None = None
    azure_storage_container: str | None = None

    azure_search_endpoint: str | None = None
    azure_search_api_key: str | None = None
    azure_search_index: str | None = None

    cfr_jar_path: str | None = None

    llm_provider: str = "stub"
    foundry_endpoint: str | None = None
    foundry_api_key: str | None = None
    foundry_model: str | None = None

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


def reset_settings_cache() -> None:
    get_settings.cache_clear()
