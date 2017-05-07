#coding=utf-8
class BasePage(object):
    base_url = "http://www.apengdai.com/"

    def __init__(self, driver, domain=base_url):
        self.driver = driver
        self.domain = domain

    def _open(self, ulr):
        url = self.domain+self.url
        self.driver.get(url)

    def open(self):
        self._open(self.url)

    def By_id(self, id):
        return self.driver.find_element_by_id(id)

    def By_name(self, name):
        return self.driver.find_element_by_name(name)

    def By_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def By_css_elements(self, css):
        return self.driver.find_elements_by_css_selector(css)

    def By_tag_name(self, tagname):
        return self.driver.find_element_by_tag_name(tagname)



