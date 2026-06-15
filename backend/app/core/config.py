from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    debug: bool
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
