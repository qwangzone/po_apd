#coding:utf-8
from selenium import webdriver
import time, unittest, os
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(file_path + "/pages")
sys.path.append(file_path + "/myunit")
sys.path.append(file_path + "/driver")
import myunit, driver
from loginpage import LoginPage
from zhitouxqpage import ZhitouxqPage


class TestZhitoutz(myunit.MyTest):
    @classmethod
    def setUpClass(self):
        self.dr = driver.browser()
        self.dr.maximize_window()
        #调用登录方法
        login_p = LoginPage(self.dr)
        login_p.login_action("15658524692", "wq123456")
        time.sleep(3)
        self.touzi_p = ZhitouxqPage(self.dr)

    def test_zhitoutz(self):
        """投资成功"""
        self.touzi_p.open()
        balance1 = self.touzi_p.my_balance().text
        balance_f1 = float(balance1.replace(',', ''))
        balance_before = int(balance_f1)
        zhifu_p = self.touzi_p.toubiao("100")
        #time.sleep(3)
        zhifu_p.zhifubutton()
        #time.sleep(3)
        zhifu_p.huishang("123456")
        time.sleep(5)
        #断言
        self.touzi_p.open()
        balance2 = self.touzi_p.my_balance().text
        balance_f2 = float(balance2.replace(',', ''))
        balance_after = int(balance_f2)
        print(balance_after)
        print(balance_before)
        self.assertEqual(100, balance_before-balance_after)

    def test_less100(self):
        """投资金额小于100元，系统给出正确提示"""
        self.touzi_p.toubiao("20")
        error_txt = self.touzi_p.error_text().text
        print(error_txt)
        self.assertEqual(error_txt, "认购金额至少 100.00 元。")

    def test_input0(self):
        """投资金额输入为0，系统给出正确提示"""
        self.touzi_p.toubiao("0")
        error_txt = self.touzi_p.error_text().text
        print(error_txt)
        self.assertEqual(error_txt, "投标金额必须大于0。")

    def test_more_input(self):
        """投资金额大于可投金额，系统给出正确提示"""
        self.touzi_p.toubiao_error("100000")
        error_txt = self.touzi_p.error_ajax().text
        #self.assertEqual(error_txt, "最大可投余额为。")
        print(error_txt)
        self.assertIn("最大可投余额为", error_txt)

    def test_than_balance(self):
        """投资金额大于账户余额，系统给出正确提示"""
        self.touzi_p.open()
        balance = self.touzi_p.my_balance().text
        balance_f = float(balance.replace(',', ''))
        balance_int = int(balance_f)
        input_number = balance_int+1
        self.touzi_p.toubiao_error(input_number)
        error_txt = self.touzi_p.error_ajax().text
        print(error_txt)
        self.assertEqual(error_txt, "余额不足请进行充值")

    @classmethod
    def tearDownClass(self):
        self.dr.quit()



if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestZhitoutz('test_zhitoutz'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    # unittest.main()

