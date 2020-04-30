
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "etl@shanghaifleetguard.com"
pwd = "sfg58657950"
receiver = "tangyc@shanghaifleetguard.com"

message = MIMEMultipart()
message['From'] = Header("BI_Server")
message['To'] = Header("IT_Operator")
message['Subject'] =Header("ETL数据处理异常提醒","utf-8")
message.attach(MIMEText("这是邮件测试内容的正文","plain","utf-8"))
try :
    server = smtplib.SMTP("smtp.shanghaifleetguard.com", 25)
    server.login(sender,pwd)
    server.sendmail(sender,[receiver],message.as_string())
    print("Success")
    server.quit()
except smtplib.SMTPException:
    print("Error:不能发送邮件")
