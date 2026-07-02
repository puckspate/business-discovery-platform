from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_ENV: str

    HOST: str
    PORT: int

    LOG_LEVEL: str

    DUCKDB_PATH: str

    class Config:
        env_file = ".env"


settings = Settings()