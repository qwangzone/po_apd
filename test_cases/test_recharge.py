import sys
import time
sys.path.append("../driver")
sys.path.append("../pages")
from loginpage import LoginPage
import driver
import unittest
class TestRecharge(unittest.TestCase):
    def setUp(self):
        self.dr = driver.browser()
        self.dr.maximize_Window()
        #调用登录方法
        login_p = LoginPage(self.dr)
        self.myacount_p = login_p.login_action("14458525690", "14458525690")

    def test_recharge(self):
        pass

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()