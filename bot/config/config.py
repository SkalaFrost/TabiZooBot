from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = 123
    API_HASH: str = '123'

    AUTO_PLAY: bool = True
    MULTIPLIER: int = 1
    MAX_PLAYS: int = 5

    UPGRADE: bool = True

    USE_REF: bool = False
    REF_ID: str = ''

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()


