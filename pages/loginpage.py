#coding=utf-8
from basepage import BasePage
import time

class LoginPage(BasePage):
    url = "user/login"

    @property
    def username_textfield(self):
        return self.By_id("userName")

    @property
    def password_textfield(self):
        return self.By_id("loginPass")

    @property
    def button_click(self):
        return self.By_tag_name("button")

    def login_action(self, username, password):
        self.open()
        self.username_textfield.send_keys(username)
        self.password_textfield.send_keys(password)
        time.sleep(5)
        self.button_click.click()

    #提示信息定位
    def null_username(self):
        return self.By_css("div.register_tis>span")

    def null_password(self):
        return self.By_css("div.register_tis.dis_ib>span")

    def alert_error(self):
        return self.By_css("div.alert-error>ul>li")





