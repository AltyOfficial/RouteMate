from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class CustomBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./environment/.env',
        extra='ignore',
    )


class AppConfig(CustomBaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str = "0.1.0"
    PROJECT_DESCRIPTION: str = "auth API"


class DatabaseConfig(CustomBaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    PG_SCHEME = "postgresql+asyncpg"

    def get_sqlalchemy_database_uri(self, scheme: str) -> str:
        return PostgresDsn.build(
            scheme=scheme,
            username=self.DB_USER,
            password=self.DB_PASS,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME,
        ).unicode_string()


class SentryConfig(CustomBaseSettings):
    SENTRY_DSN: str


class MainConfig(BaseModel):
    app: AppConfig = AppConfig()
    db: DatabaseConfig = DatabaseConfig()
    sentry: SentryConfig = SentryConfig()


settings = MainConfig()
