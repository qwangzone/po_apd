from HTMLTestRunner import HTMLTestRunner
import unittest, time, os
# file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# file_path1 = os.path.dirname(os.path.abspath(__file__))
# file_path2 = os.path.abspath(__file__)
# print("file_path1" + file_path1)
# print("file_path2" + file_path2)
# print("file_path" + file_path)
dir = "./test_cases"
discover = unittest.defaultTestLoader.discover(dir, pattern="test_*.py", top_level_dir=None)
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp, title="阿朋贷测试报告", description="环境：win10，浏览器：chrome")
runner.run(discover)