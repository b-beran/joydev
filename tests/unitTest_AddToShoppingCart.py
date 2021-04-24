import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()

    def test_cms(self):
        user = "Admin"
        pwd = "p@ssword"

        driver = self.driver
        driver.maximize_window()
        # driver.get("http://127.0.0.1:8000/admin")
        # elem = driver.find_element_by_id("id_username")
        # elem.send_keys(user)
        # elem = driver.find_element_by_id("id_password")
        # elem.send_keys(pwd)
        # time.sleep(5)
        # elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(5)
        # assert "Logged in"
        # find a product
        elem = driver.find_element_by_link_text("Enter the 36 Chambers").click()
        time.sleep(5)
        continue_test = False
        try:
            elem = driver.find_element_by_xpath("/html/body/div[3]/div/form/input[3]").click()
            continue_test = True

        except NoSuchElementException:
            self.fail("Add to Cart does not appear = Add to Cart button not present")
            assert False
            time.sleep(5)
        time.sleep(5)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
