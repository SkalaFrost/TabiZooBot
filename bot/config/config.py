from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = 20546282
    API_HASH: str = '4bef5eb0d3ee75bb4e83e800d2b1d773'

    UPGRADE: bool = True

    USE_REF: bool = False
    REF_ID: str = ''

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()


