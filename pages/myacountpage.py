#coding=utf-8
from basepage import BasePage
class MyacountPage(BasePage):
    def login_success_text(self):
        return self.By_css("li.subNav>a")

    def balance(self):
        pass
