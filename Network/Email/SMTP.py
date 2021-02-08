import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

sender = '13015754199@163.com'
passwd = ''
user = '546393338@qq.com'

def sendmail():
    passwd = input("Enter password of {}".format(sender))
    try:
        msg = MIMEText('1','plain','utf-8')
        msg['From'] = formataddr(["Zachary",sender])
        msg['To'] = formataddr(["Mr_Strawberry",user])
        msg['Subject'] = "Testing mail"

        s = smtplib.SMTP("smtp.163.com", 25)
        s.login(sender, passwd)
        s.sendmail(sender,[user,],msg.as_string())
        s.quit()
        print("send mail succseefully!")
    except Exception as e:
        print("failed to send mail!", e)


sendmail()