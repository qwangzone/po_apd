from HTMLTestRunner import HTMLTestRunner
import unittest, time, os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
# file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# file_path1 = os.path.dirname(os.path.abspath(__file__))
# file_path2 = os.path.abspath(__file__)
# print("file_path1" + file_path1)
# print("file_path2" + file_path2)
# print("file_path" + file_path)

#=========定义发送邮件==========
def send_mail(file_new):
    with open(file_new, 'rb') as f:
        mail_body = f.read()
    print(file_new + "调用后")
    #print(mail_body)
    # msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    #发送内容为HTML的邮件
    # msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
    #发送内容为普通文本的邮件
    # msg = MIMEText("python发邮件测试", _charset='utf-8')
    #发送带附件的邮件
    msg = MIMEMultipart()
    #构造附件
    att1 = MIMEText(mail_body, 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="wq.html"'
    msg.attach(att1)
    #msg.attach(MIMEText("阿朋贷自动化测试报告", 'plain', 'utf-8'))
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
    msg['Subject'] = Header("阿朋贷最新自动化测试报告", 'utf-8')
    msg['From'] = 'sad120@126.com'
    msg['To'] = 'qiwang01@rongxinchina.net'
    #连接smtp服务器
    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("sad120@126.com", "wq15803863660@") #用户名与密码
    smtp.sendmail("sad120@126.com", "qiwang01@rongxinchina.net", msg.as_string())
    smtp.quit()
    print("邮件已发送!!")
if __name__ == '__main__':

    dir = "./test_cases"
    discover = unittest.defaultTestLoader.discover(dir, pattern="test_login.py", top_level_dir=None)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + 'result.html'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = base_dir + "/report/" + filename
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title="阿朋贷测试报告", description="环境：win10，浏览器：chrome")
    runner.run(discover)
    print(filename+"调用前")
    send_mail(file_name)