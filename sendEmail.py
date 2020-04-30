import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendEmail(msg):
    if len(msg) != 0:
        #初始化用户信息
        sender = "xxxxxxx@xxxx.com"   #sender account
        passwd = "asdfasdfasdf"                  #sender passwd
        receiver = "xxxxx@xxx.com"    #target account
        
        errorMsg = "<p>ETL数据处理异常结果如下：</p>"
        for i in range(len(msg)):
            errorMsg += "<p>"+msg[i]+"</p>"
        message = MIMEText(errorMsg,'html','utf-8')
        message['From'] = Header("BI_Server")   #发送人简称
        message['To'] = Header("IT_Operator")   #收件人简称
        message['Subject'] = Header("ETL数据处理异常提醒")  #邮件主题
        
        try:
            server = smtplib.SMTP("xxxxxx@xxx.com", 25)   #server
            server.login(sender,passwd)
            server.sendmail(sender,[receiver],message.as_string())
            server.quit()
            return 1
        except smtplib.SMTPException:
            return -1
