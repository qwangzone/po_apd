from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# dr = webdriver.Chrome()
# dr.get("http://www.baidu.com")
# title = EC.presence_of_element_located('id', 'kw')(dr).send_keys("java")
# time.sleep(9)
# print(title(dr))
# #element = WebDriverWait(driver=dr, timeout=5, poll_frequency=1).until(lambda x: x.find_element_by_id('kww'))
# if WebDriverWait(driver=dr, timeout=5, poll_frequency=1).until(lambda x: x.find_element_by_id('kww')):
#     #print(type(element))
#     #print(element)
#     element = WebDriverWait(driver=dr, timeout=5, poll_frequency=1).until(lambda x: x.find_element_by_id('kww'))
#     element.send_keys('python')
# else:
#     print("元素找不到")
# #WebDriverWait(driver=dr, timeout=5, poll_frequency=1).until_not(lambda x: x.find_element_by_id('su')).click()

class add:
    def __int__(self, *args):
    def sum(self, *args):
        for i in args:
            print(i)

a=('id', 'userName')
b = add(