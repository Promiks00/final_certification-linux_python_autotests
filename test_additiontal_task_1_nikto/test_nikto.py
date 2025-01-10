from .checkers import checkout
import logging
import yaml

with open("./data.yaml") as f:
    data = yaml.safe_load(f)

def test_step01():
    logging.info("Site check started...")
    cmd = f"nikto -h {data['check_url']} -ssl -Tuning 4"
    success = checkout(cmd, "0 error(s)")
    assert success, f"Test 1 FAIL: Nikto scan failed on {data['check_url']}"
    logging.info("Checking complete")