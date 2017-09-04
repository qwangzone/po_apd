#coding:utf-8
from selenium import webdriver
import time, unittest
import sys
sys.path.append("..\pages")
sys.path.append("..\myunit")
sys.path.append("..\driver")
import myunit
from loginpage import LoginPage
from zhitouxqpage import ZhitouxqPage


class TestZhitoutz(myunit.MyTest):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        #调用登录方法
        login_p = LoginPage(self.dr)
        login_p.login_action("14458524699", "14458524699")
        time.sleep(3)
        self.touzi_p = ZhitouxqPage(self.dr)

    def test_zhitoutz(self):
        """投资成功"""
        zhifu_p = self.touzi_p.toubiao("100")
        time.sleep(3)
        zhifu_p.zhifubutton()
        time.sleep(3)
        #断言

    def test_less100(self):
        """投资金额小于100元，系统给出正确提示"""
        self.touzi_p.toubiao("20")
        error_txt = self.touzi_p.error_text().text
        self.assertEqual(error_txt, "认购金额至少 100.00 元。")

    def test_input0(self):
        """投资金额输入为0，系统给出正确提示"""
        self.touzi_p.toubiao("0")
        error_txt = self.touzi_p.error_text().text
        self.assertEqual(error_txt, "投标金额必须大于0。")

    def test_more_input(self):
        """投资金额大于可投金额，系统给出正确提示"""
        self.touzi_p.toubiao("1000000")
        error_txt = self.touzi_p.error_text().text
        self.assertEqual(error_txt, "该项目可认购金额不足。")

    def test_than_balance(self):
        """投资金额大于账户余额，系统给出正确提示"""
        self.touzi_p.open()
        balance = self.touzi_p.my_balance().text
        balance_f = float(balance.replace(',', ''))
        balance_int = int(balance_f)
        input_number = balance_int+1
        self.touzi_p.toubiao(input_number)
        error_txt = self.touzi_p.error_text().text
        self.assertEqual(error_txt, "对不起，您的账户余额小于投标金额。")

    def tearDown(self):
        self.dr.quit()



if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestZhitoutz('test_zhitoutz'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    #unittest.main()

