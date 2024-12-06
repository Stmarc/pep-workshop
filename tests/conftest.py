from src.configs import EnvConfig
from src.configs import UserConfig
import requests
import pytest


@pytest.fixture(scope="session")
def env_config() -> EnvConfig:
    """Enviroment variables (like url)"""
    return EnvConfig()


@pytest.fixture(scope="session")
def user_config() -> UserConfig:
    """Usersname"""
    return UserConfig()


@pytest.fixture(scope="session")
def token(user_config, env_config) -> str | None:
    print(user_config.model_dump_json)
    respons: requests.Response = requests.post(url=f"{env_config.url}/auth", data=user_config.model_dump())
    if respons.status_code != 200:
        return None
    if "token" not in respons.json():
        return None

    return respons.json()["token"]
