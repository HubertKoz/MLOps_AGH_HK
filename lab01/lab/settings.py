# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator

ALLOWED_ENVIRONMENTS = ("dev", "test", "prod")


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    ASDF: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        if value not in ALLOWED_ENVIRONMENTS:
            raise ValueError(f"Env '{value}' not allowed")  # implement me!
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        return value
