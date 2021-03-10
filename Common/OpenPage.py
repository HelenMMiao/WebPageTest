import unittest
import time
from selenium import webdriver

class GmailLoginTest(unittest.TestCase):
    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('tear down')

    def test_1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://accounts.google.com/Login')
        driver.implicitly_wait(2)
        driver.find_element_by_id('identifierId').send_keys('TTtestTTtestTT1@gmail.com')
        time.sleep(2)
        driver.find_element_by_xpath('//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[2]').click()
        driver.find_element_by_name('password').send_keys('Roblox123')
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()