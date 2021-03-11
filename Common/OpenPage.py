import unittest
import time
from selenium import webdriver
from ddt import ddt, data, unpack


def readUserData():
    file = open('IDPWD.txt', mode='r', encoding='utf8')
    NamePwds = []

    for line in file.readlines():
        NamePwds.append(line.strip('\n').split(','))

    file.close()
    return NamePwds




@ddt
class GmailLoginTest(unittest.TestCase):

    #Open login page
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://accounts.google.com/Login')
        self.driver.implicitly_wait(10)

    #Close web broser
    def tearDown(self) -> None:
        self.driver.quit()

    #Login using different username/password
    @data(*readUserData())
    @unpack
    def test_1(self, username,password):
        self.driver.find_element_by_id('identifierId').send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_xpath('//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[2]').click()
        self.driver.find_element_by_name('password').send_keys(password)
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()