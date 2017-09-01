import unittest
import sys
sys.path.append("../driver")
import driver
class MyTest(unittest.TestCase):
    def setUp(self):
        self.dr = driver.browser()
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    class Test(MyTest):
        def test_case(self):
            self.dr.get("http://www.baidu.com")

    unittest.main()