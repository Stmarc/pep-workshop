import requests
from pytest_check import check

from http import HTTPStatus


def test_valid(user_config, env_config_auth_url):
    # json: dict[str,str]={"username":user_config.username,"password":user_config.password}
    print(user_config.model_dump_json)
    respons: requests.Response = requests.post(url=env_config_auth_url, data=user_config.model_dump())
    with check:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
        assert "token" in respons.json()

    with check:
        print("3")
        assert respons.status_code == HTTPStatus.OK

    print(respons.json())
