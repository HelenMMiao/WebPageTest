from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, os
import unittest

class temp(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        self.driver.quit()

    def saveImage(self):
        timeAppendix = time.strftime('%H%M%S', time.localtime(time.time()))
        screenFile = 'C:\DevTesters\PycharmProjects\WebPageTest\Pictures\Login' + timeAppendix + '.png'
        self.driver.save_screenshot(screenFile)

    def test_1(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # driver.get('https://accounts.google.com/Login')
        self.driver.implicitly_wait(3)
        try:
            ele = self.driver.find_element_by_id('password')
            ele.send_keys("Miao")
        except NoSuchElementException:
            print("wo zhao bu dao")
            self.saveImage()

if __name__ == '__main__':
    unittest.main()