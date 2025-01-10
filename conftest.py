import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser():
    logging.info("Setting up Chrome browser...")
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    logging.info("Chrome browser started successfully.")
    yield driver
    logging.info("Closing the Chrome browser...")
    driver.quit()
    logging.info("Chrome browser closed.")