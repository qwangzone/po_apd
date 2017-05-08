from basepage import BasePage

class ZhitouzfPage(BasePage):

    def zhifubutton(self):
        #return self.By_tag_name("button")
        return self.By_css("div.affirm_bt>span")


