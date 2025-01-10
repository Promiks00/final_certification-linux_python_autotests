import requests
import yaml
import logging

with open("./config.yaml") as f:
    data = yaml.safe_load(f)

def test_user_profile(login):
    token, user_id = login
    header = {"X-Auth-Token": token}

    logging.info(f"Sending request to fetch profile for user_id {user_id}...")

    response = requests.get(f"{data['address']}/api/users/profile/{user_id}", headers=header)
    response.raise_for_status()

    logging.info(f"Received response for user_id {user_id}. Checking username...")

    expected_username = data["username"]
    actual_username = response.json().get("username")

    assert  expected_username == actual_username, f"Expected username {expected_username} but got {actual_username}"
    logging.info("Test passed, username matches.")