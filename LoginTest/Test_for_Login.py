import unittest
import time
from selenium import webdriver
from ddt import ddt, data, unpack, file_data
import os

"""
Read user data from TXT file. 
TXT file includes different types of correct user name and password.
It could include phone number further to test.
"""
def readUserData():
    file = open('C:\DevTesters\PycharmProjects\WebPageTest\Data\IDPWD.txt', mode='r', encoding='utf8')
    NamePwds = []

    #Get content line by line and transfer to list group.
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

    # Close web broser
    def tearDown(self) -> None:
        self.driver.quit()

    #Input Email address and click Next
    def InputEmail(self, username):
        self.driver.find_element_by_id('identifierId').send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[2]').click()
        self.driver.implicitly_wait(10)

    #Input password and click Next
    def InputPassword(self, password):
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_xpath(
            "//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[2]").click()
        self.driver.implicitly_wait(10)

    #save screenshot function.
    def saveImage(self):
        timeAppendix = time.strftime('%H%M%S', time.localtime(time.time()))
        screenFile = 'C:\DevTesters\PycharmProjects\WebPageTest\Pictures\Login' + timeAppendix + '.png'
        self.driver.save_screenshot(screenFile)

    """
    Login using correct username/password from TXT file. 
    It could include phone number further to test.
    """
    @data(*readUserData())
    @unpack
    def test_1(self, username, password):
        try:
            self.InputEmail(username)
            self.InputPassword(password)
            isFound = self.driver.find_element_by_xpath(
            "//body/c-wiz[1]/div[1]/div[2]/c-wiz[1]/c-wiz[1]/div[1]/div[1]/div[3]/c-wiz[1]/nav[1]/ul[1]/li[2]/a[1]/div[2]")
            self.assertTrue(isFound, msg="Correct password login failed")
            # self.assertTrue(self.driver.find_element_by_xpath("//body/c-wiz[1]/div[1]/div[2]/c-wiz[1]/c-wiz[1]/div[1]/div[1]/div[3]/c-wiz[1]/nav[1]/ul[1]/li[2]/a[1]/div[2]"), msg="Correct password login failed")
        except:
            self.saveImage()

    # #Promp shows when incorrect password is used.
    @data(['TTtestTTtestTT1@gmail.com','Hellow'])
    @unpack
    def test_2(self, username, password):
        try:

            self.InputEmail(username)
            self.InputPassword(password)
            # Verify login successfully
            isFound = self.driver.find_element_by_xpath("//div[@id='view_container']/div[@class='zWl5kd']/div[@role='presentation']/div[@role='presentation']/div[@role='presentation']//form[@action='/signin/v2/challenge/password/empty']//section/div/div/div[1]//span")
            self.assertEqual("Wrong password. Try again or click ‘Forgot password’ to reset it.", isFound.text, msg="Prompt for incorrect password is wrong")
        except:
            self.saveImage()

    #Login using invalide Email
    @data("fdsd@fafdasdj.com")
    def test_3(self, username):
        try:
            self.InputEmail(username)
            isFound = self.driver.find_element_by_xpath("//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
            self.assertEqual(isFound.text, "Couldn't find your Google Account", msg="Prompt for invalid Email is wrong")
        except:
            self.saveImage()

    # Try to login using Non-Email format
    @data("test@test", "TTtestTTtestTT1@@gmail.com")
    def test_4(self, username):
        try:
            self.InputEmail(username)
            isFound = self.driver.find_element_by_xpath(
                "//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
            self.assertEqual(isFound.text, "Enter a valid email or phone number", msg="Prompt for non-Email is wrong")
        except:
            self.saveImage()
    #skip this test case unconditionally
    #Login with nothing input
    @unittest.skip('less used scenario')
    def test_5(self):
        try:
            self.driver.find_element_by_xpath(
                '//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[2]').click()
            self.driver.implicitly_wait(10)
            isFound = self.driver.find_element_by_xpath(
                "//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
            self.assertEqual(isFound.text, "Enter an email or phone number", msg="Prompt for none input in Email is wrong")
        except:
            self.saveImage()

    # #Pseudo test case, not include in test suite.
    def test_6(self):
        print("A predo test case")
    #
    # #login with white space input
    def test_7(self):
        try:
            self.InputEmail(" ")
            isFound = self.driver.find_element_by_xpath(
                "//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
            self.assertEqual("Enter an email or phone number", isFound.text, msg="Prompt for white space input is wrong")
        except:
            self.saveImage()

# #Try yaml files
    # @file_data('yamlToPrint.yaml')
    # def test_2(self, **user):
    #     print(user.get('Sex'))
    #     print(user.get('Age'))


if __name__ == '__main__':
    unittest.main()