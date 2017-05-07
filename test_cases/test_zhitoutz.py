from selenium import webdriver
import time, unittest


class TestZhitoutz(unittest.TestCase):
    def setUp(self):
        self.dr=webdriver.Chrome()
        self.dr.maximize_window()

    def test_zhitoutz(self):
        #调用登录方法

