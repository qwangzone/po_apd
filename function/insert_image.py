from selenium import webdriver
import os
#截图函数
def insert_image(driver,image_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = base_dir + '/report/screenshot_image/' + image_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    insert_image(driver, "baidu.jpg")
    driver.quit()