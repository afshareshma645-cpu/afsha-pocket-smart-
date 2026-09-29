from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Pocket Smart AI"

settings = Settings()