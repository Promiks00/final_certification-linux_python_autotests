from testpage import OperationsHelper
import logging
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
   data = yaml.safe_load(f)

name = data["username"]
passwd = data["password"]
site = data["address"]

class TestNegative:
    def test_step01_auth_negative(self, browser):
        logging.info("Test1 Starting")
        testpage = OperationsHelper(browser)
        testpage.go_to_site()
        testpage.enter_login("test")
        testpage.enter_pass("test")
        testpage.click_login_button()
        error_text = testpage.get_error_text()
        assert error_text == "401"
        logging.info("Test1 Completed")


class TestPositive:
    def test_step02_auth_positive(self, browser):
        logging.info("Test2 Starting")
        testpage = OperationsHelper(browser)
        testpage.enter_login(name)
        testpage.enter_pass(passwd)
        testpage.click_login_button()
        user_text = testpage.get_user_text()
        assert user_text == f"Hello, {name}"
        logging.info("Test2 Completed")

    def test_step03_click_about_link(self, browser):
        logging.info("Test3 Starting")
        testpage = OperationsHelper(browser)
        testpage.click_about_link()
        about_text = testpage.get_about_text()
        assert about_text == "About Page"
        logging.info("Test3 Completed")

    def test_step04_get_fontsize_value_of_title_on_page_About(self,browser):
        logging.info("Test4 Starting")
        testpage = OperationsHelper(browser)
        value = testpage.get_property_value_title()
        assert value == "32px", f"Expected font-size value of title on page 'About' as '32px', but got '{value}'"
        logging.info("Test4 Completed")