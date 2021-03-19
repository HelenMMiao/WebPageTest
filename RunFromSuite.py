import unittest
from LoginTest.Test_for_Login import GmailLoginTest
import os
from HTMLTestRunner import HTMLTestRunner


#Create a test suite
suite = unittest.TestSuite()

'''There are five ways to add test cases.'''
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
# method 5 to add test cases. Do not need to import.
# suite.addTest(unittest.TestLoader().loadTestsFromName('LoginTest.Test_for_Login.GmailLoginTest'))



# Run cases in suite
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
    # runner.run(discover)


'''Generate test report using HTMLTestRunner'''
# Define report's name and title
report_name = "Test Report.html"
report_path = './Report/'
report_file = report_path + report_name
report_title = "Test Result for login module"
report_description = "Test result for login module with both valid and invalid input, also covering error guessing input"

#Create report folder if it does not exist.
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass

#run cases from HTMLRunner and generate report
with open(report_file, 'w') as report:
    runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=report_title, description=report_description)
    runner.run(suite)