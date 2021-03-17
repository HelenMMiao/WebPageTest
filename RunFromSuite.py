import unittest
from LoginTest.Test_for_Login import GmailLoginTest



# cases = [GmailLoginTest('test_1'), GmailLoginTest('test_4'), GmailLoginTest('test_3'), GmailLoginTest('test_2')]

#Create a test suite
suite = unittest.TestSuite()


'''There are three ways to add test cases.'''
# method 1 to add test cases, one by one
# suite.addTest(GmailLoginTest('test_6'))
# suite.addTest(GmailLoginTest('test_7'))
# method 2 to add test case, from list
# cases = [GmailLoginTest('test_6'), GmailLoginTest('test_7')]
# suite.addTests(cases)
# method 3 to add test cases, all cases in both Test_for_Login.py & Test_for_Demo.py
# test_dir = './LoginTest'
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test_for*py')
# method 4 to add test cases. all cases in GmailLoginTest class
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(GmailLoginTest))
# method 5 to add test cases
# suite.addTest(unittest.TestLoader().loadTestsFromName('LoginTest.Test_for_Login.GmailLoginTest'))



#Run cases in suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # runner.run(discover)