import pytest
import yaml
import requests

with open("./test_additional_task_2_auth/config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    login = requests.post(f"{data["address"]}/gateway/login",
                          data={"username": data["username"], "password": data["password"]})
    token = login.json()["token"]
    user_id = login.json()["id"]
    return token, user_id