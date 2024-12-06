import requests
from pytest_check import check

from http import HTTPStatus


def test_ping_valid(env_config_ping_url):
    respons: requests.Response = requests.get(url=env_config_ping_url)
    print(respons)
    with check:
        print("???????????????/")
        assert respons.status_code == 201
