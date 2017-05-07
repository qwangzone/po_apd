#coding=utf-8
from basepage import BasePage
class MyacountPage(BasePage):
    def success_text(self):
        return self.By_css("li.subNav>a")