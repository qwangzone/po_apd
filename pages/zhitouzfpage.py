from basepage import BasePage

class ZhitouzfPage(BasePage):

    def zhifubutton(self):
        #return self.By_tag_name("button")
        js = "document.getElementsByClassName('affirm_qr_bt')[0].click()"
        #return self.By_css("div.affirm_bt>span")
        self.driver.execute_script(js)


    def huishang(self, password):
        self.My_wait(('id', 'pass')).send_keys(password)
        #self.By_id("pass").send_keys(password)
        self.By_id("sub").click()


