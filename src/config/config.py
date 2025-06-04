from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    bot_token: SecretStr
    db_url: SecretStr
    
    model_config = SettingsConfigDict(env_file=".env")

config = Settings()