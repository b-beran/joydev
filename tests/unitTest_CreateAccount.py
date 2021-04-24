import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# before running this test, ensure:
    # user account does not already exist
    # users are logged out
    # you have the right browser extension selected for your demo (lines 14-15)

class CreateAccount(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()


    def testSignUp(self):
        username = "jaddams"
        first = "jane"
        last = "addams"
        email = "jaddams@hullhouse.org"
        password = "hullrocks"
        passconf = "hullrocks"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)

        # click Signup link
        elem = driver.find_element_by_link_text("Signup").click()
        time.sleep(3)

        # sign up
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(username)
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys(first)
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys(last)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys(email)
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys(password)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys(passconf)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)

        # assert signed up - find Logout link
        try:
            elem = driver.find_element_by_link_text("Logout")
            assert True

        except NoSuchElementException:
            self.fail("Signup failed")
            assert False

        time.sleep(5)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()