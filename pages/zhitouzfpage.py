from basepage import BasePage

class ZhitouzfPage(BasePage):

    def zhifubutton(self):
        #return self.By_tag_name("button")
        js = "document.getElementsByClassName('affirm_qr_bt')[0].click()"
        #return self.By_css("div.affirm_bt>span")
        self.driver.execute_script(js)


