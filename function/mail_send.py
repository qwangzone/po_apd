import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
class SendMail:
    def __init__(self, send_address, send_address_password, received_address,
                 mail_body, subject, content, subtype='plain'):
        self.send_address = send_address
        self.send_address_password = send_address_password
        self.received_address = received_address
        self.subject = subject
        self.content = content
        self.subtype = subtype
        self.mail_body = mail_body

    def send_mail(self):
        msg = MIMEMultipart()
        # 定义正文
        # msg = MIMEText(self.content, _subtype=self.subtype, _charset='utf-8')
        msg.attach(MIMEText(self.content, _subtype=self.subtype, _charset='utf-8'))
        #定义主题
        msg['Subject'] = Header(self.subject, 'utf-8')
        msg['From'] = self.send_address
        msg['To'] = self.received_address
        #定义附件
        att1 = MIMEText(self.mail_body, 'base64', 'utf-8')
        att1['Content-Type'] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="wq.html"'
        msg.attach(att1)
        #连接邮箱服务器，发送邮件
        smtp = smtplib.SMTP()
        smtp.connect("smtp.126.com")
        smtp.login(self.send_address, self.send_address_password)
        smtp.sendmail(self.send_address, self.received_address, msg.as_string())

        smtp.quit()
        print("邮件发送成功！")

if __name__ == '__main__':
    send_addr = "sad120@126.com"
    send_addr_pass = "wq15803863660@"
    received_addr = "qiwang01@rongxinchina.net"
    sub = "银行账单测试"
    subt = 'html'
    cont = "您的银行卡已入账1000万，请注意查收————测试"

    wq = SendMail(send_addr, send_addr_pass, received_addr, sub, cont, subtype=subt)
    wq.send_mail()