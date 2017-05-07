from basepage import BasePage
from zhitouzfpage import ZhitouzfPage


class ZhitouxqPage(BasePage):
    url = "project/in fo/11084"

    @property
    def money_text(self):
        return self.By_id("amount")

    @property
    def touzi_button(self):
        return self.By_css("input[type='submit']")

    def toubiao(self, money):
        self.money_text.sendkeys("100")
        self.touzi_button.click()
        return ZhitouzfPage(self.driver)



