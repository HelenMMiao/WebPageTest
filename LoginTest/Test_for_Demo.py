import unittest

class DemoClass(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_1(self):
        print("test case 1 in demo test")
    def test_2(self):
        print("test case 2 in demo test")

if __name__ == '__main__':
    unittest.main()