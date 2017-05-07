#coding=utf-8
import sys
sys.path.append("..\pages")
from loginpage import LoginPage
from myacountpage import MyacountPage
import unittest, time
from selenium import webdriver



class TestLogin(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    #登录成功
    def test_login_success(self):
        login_p = LoginPage(self.dr)
        login_p.login_action("wq1qaz_", "wq15803863660")
        myacount_p = MyacountPage(self.dr)
        time.sleep(3)
        assert_text = myacount_p.success_text().text
        print (assert_text)
        self.assertEqual(u"账户总览", assert_text,msg = "++++++++++++++")

    #用户名、密码输入为空，系统提示输入用户名与密码
    def test_null_username_password(self):
        login_p = LoginPage(self.dr)
        login_p.login_action("", "")
        null_username_text = login_p.null_username().text
        null_password_text = login_p.null_password().text
        self.assertIn(u"用户名或手机号", null_username_text)
        self.assertIn(u"填写密码", null_password_text)

    #用户名输入为空，密码正确输入，系统提示输入用户名
    def test_null_username(self):
        login_p = LoginPage(self.dr)
        login_p.login_action("", "123456")
        null_username_text = login_p.null_username().text
        self.assertIn(u"用户名或手机号", null_username_text)

    #用户名正确输入，密码输入为空，系统提示输入密码
    def test_null_passoword(self):
        login_p = LoginPage(self.dr)
        login_p.login_action("wq1qaz_", "")
        null_password_text = login_p.null_password().text
        self.assertIn(u"填写密码", null_password_text)

    def tearDown(self):
        self.dr.quit()
if __name__ == '__main__':
    """
    suit = unittest.TestSuite()
    suit.addTest(TestLogin('test_null_username_password'))
    suit.addTest(TestLogin('test_login_success'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    """
    unittest.main()



