import requests
from pytest_check import check


def test_notvalid(user_config,env_config_auth_url):
    json: dict[str,str]={"username":user_config.username,"password":user_config.password+"1"}
    respons: requests.Response = requests.post(url=env_config_auth_url,json=json)
    with check:
        print("!!!!!!!!!!!!!!!!!!1")
        assert "token" not in respons.json()

    with check:
        print("1")
        assert respons.status_code == 200


def test_valid_with_extrafield(env_config_auth_url,user_config):
    json=user_config.model_dump()
    json["extra"]="some_value"
    respons: requests.Response = requests.post(url=env_config_auth_url,json=json)
    with check:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        assert "token" in respons.json()
    with check:
        print("2")
        assert respons.status_code == 200
    print(respons.json())
