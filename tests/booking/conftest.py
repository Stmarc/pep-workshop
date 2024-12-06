from src.configs import UserConfig
import pytest



@pytest.fixture(scope="session")
def env_config_booking_url(env_config) -> str:
    """Enviroment variables (like url)"""
    return f"{env_config.url}/booking"