import unittest
import re
from Test_for_Login import GmailLoginTest

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test_for*py')

for dis in discover:
    print(dis)