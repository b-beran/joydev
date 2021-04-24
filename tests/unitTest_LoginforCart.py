import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# before running this test, ensure:
    # user account exists (you ran the unitTest_CreateAccount test)
    # users are logged out
    # you have a product with the name "UB40 Signing Off"
    # you have the right browser extension selected for your demo (lines 16-17)

class LoginforCart(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()

    def test_login(self):
        user = "jaddams"
        pwd = "hullrocks"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")

        # navigate to product and add to cart
        elem = driver.find_element_by_link_text("UB40 Signing Off").click()
        time.sleep(3)
        add_to_cart_button = driver.find_elements_by_xpath('//*[@id="content"]/div/form/input[3]')[0]
        add_to_cart_button.click()
        time.sleep(3)

        # assert asked for login
        try:
            elem = driver.find_element_by_id("id_username")
            assert True

        except NoSuchElementException:
            self.fail("Cart login failed")
            assert False

        time.sleep(5)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
