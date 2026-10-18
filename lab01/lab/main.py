import os
import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml


def export_envs(environment: str = "dev") -> None:
    env_path = os.path.join(os.getcwd(), "config", f".env.{environment}")
    load_dotenv(env_path)


def load_secrets(secrets_path: str = "secrets.yaml") -> None:
    with open(secrets_path, "r") as f:
        for key, val in yaml.safe_load(f).items():
            os.environ[key] = str(val)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    load_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("ASDF: ", settings.ASDF)
