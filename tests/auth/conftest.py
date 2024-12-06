from src.configs import EnvConfig
from src.configs import UserConfig
import pytest


# @pytest.fixture(scope="session")
# def env_config_url() -> str:
#     """Enviroment variables (like url)"""
#     return EnvConfig.url


@pytest.fixture(scope="session")
def env_config_auth_url(env_config) -> str:
    """Enviroment variables (like url)"""
    return f"{env_config.url}/auth"
