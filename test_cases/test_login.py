#coding=utf-8
import sys, os
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(file_path)
sys.path.append(file_path + "/pages")
sys.path.append(file_path + "/driver")
from loginpage import LoginPage
from myacountpage import MyacountPage
import unittest, time, driver
from selenium import webdriver
from parameterized import parameterized

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dr = driver.browser()
        self.dr.maximize_window()
        self.login_p = LoginPage(self.dr)
    @parameterized.expand([("pwd_error", "1445854699", "14458524699", "用户名或密码不正确"),
                           ("user_error", "14458524699", "1448524699", "用户名或密码不正确")])
    #参数化用例,登录失败情况
    def test_login(self, name, username, password, assert_text):
        self.login_p.login_action(username, password)
        time.sleep(2)
        error_text = self.login_p.alert_error().text
        print(error_text)
        self.assertEqual(error_text, assert_text)

    #登录成功
    def test_login_success(self):
        #login_p = LoginPage(self.dr)
        myacount_p = self.login_p.login_action("14458525690", "14458525690")
        print(self.dr.current_url)
        #myacount_p = MyacountPage(self.dr)
        time.sleep(3)
        assert_text = myacount_p.login_success_text().text
        print(assert_text)
        self.assertEqual(u"账户总览", assert_text, msg="++++++++++++++")
    """
    #用户名、密码输入为空，系统提示输入用户名与密码
    def test_null_username_password(self):
        #login_p = LoginPage(self.dr)
        self.login_p.login_action("", "")
        null_username_text = self.login_p.null_username().text
        null_password_text = self.login_p.null_password().text
        self.assertIn(u"用户名或手机号", null_username_text)
        self.assertIn(u"填写密码", null_password_text)

    #用户名输入为空，密码正确输入，系统提示输入用户名
    def test_null_username(self):
        #login_p = LoginPage(self.dr)
        self.login_p.login_action("", "123456")
        null_username_text = self.login_p.null_username().text
        self.assertIn(u"用户名或手机号", null_username_text)

    #用户名正确输入，密码输入为空，系统提示输入密码
    def test_null_passoword(self):
        #login_p = LoginPage(self.dr)
        self.login_p.login_action("wq1qaz_", "")
        null_password_text = self.login_p.null_password().text
        self.assertIn(u"填写密码", null_password_text)
    """

    @classmethod
    def tearDownClass(self):
        self.dr.quit()
if __name__ == '__main__':
    # suit = unittest.TestSuite()
    # #suit.addTest(TestLogin('test_login_success'))
    # suit.addTest(TestLogin('test_login_success'))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)

    unittest.main()



