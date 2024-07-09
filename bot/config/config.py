from dataclasses import dataclass
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    BOT_TOKEN: str

    @property
    def ASYNC_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def GET_BOT_TOKEN(self):
        return f"{self.BOT_TOKEN}"

    class Config:
        env_file = '.env'


@dataclass
class Config:
    tg_bot: Settings
    db: Settings


def load_config() -> Config:
    bot = Settings()
    db_settings = Settings()

    return Config(
        tg_bot=bot,
        db=db_settings
    )