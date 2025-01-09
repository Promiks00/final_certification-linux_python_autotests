from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

class TestSearchLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = By.XPATH, locators["xpath"][locator]
    for locator in locators["css"].keys():
        ids[locator] = By.CSS_SELECTOR, locators["css"][locator]

class OperationsHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = None

    # ENTER_TEXT
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    # ENTER_TEXT locator methods
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")


    # CLICK
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.error(f"Exception while clicking on {element_name}")
            return False
        logging.debug(f"Element {element_name} was clicked")
        return True

    # CLICK locator methods
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login button")

    def click_about_link(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ABOUT_LINK"], description="about link")

    # GET_VALUE
    def get_value_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        try:
            value = self.get_element_property(locator, testdata["find_value"])
            if value is None:
                logging.error(f"Value not found for {element_name}")
            else:
                logging.debug(f"Found value {value} for {element_name}")
            return value
        except:
            logging.exception(f"Exception while getting value for {element_name}")
            return None

    # GET_VALUE locator methods
    def get_property_value_title(self):
        return self.get_value_from_element(TestSearchLocators.ids["LOCATOR_ABOUT_TITLE"], description="value")