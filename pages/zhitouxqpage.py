#coding:utf-8
from basepage import BasePage
from zhitouzfpage import ZhitouzfPage
import time


class ZhitouxqPage(BasePage):
    url = "/licai/12352"

    @property
    def money_text(self):
        return self.By_id("amount")

    @property
    def touzi_button(self):
        return self.By_css("input[type='submit']")

    @property
    def queren(self):
        return self.By_id("okcp")


    def toubiao(self, money):
        self.open()
        time.sleep(3)
        self.money_text.send_keys(money)
        self.touzi_button.click()
        self.queren.click()
        return ZhitouzfPage(self.driver)

    #错误提示
    def error_text(self):
        return self.By_css("div.alert-error>ul>li")

    #账户余额
    def my_balance(self):
        return self.By_css("p[id='zhanghu']>span")





