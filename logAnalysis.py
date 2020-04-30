import fileProcess
import readPathFiles
import sendEmail

import datetime
import sys

def main():
    #filePath = input("请输入日志文件目录：")
    logResult = []
    resultCode = 0
    count = 0
    filePath = "C:/Users/Administrator/Documents/BI-Projects/6-Logs"
    #filePath = "C:/Users/shfg/Documents/2.0 资料文档/6-Logs"
    if len(filePath) != 0 :
        #获取文件列表以及文件的最新日期
        fileDict,maxDate = readPathFiles.readPathFiles(filePath)
        if fileDict :
            strMaxDate = datetime.datetime.strftime(maxDate,"%Y-%m-%d")
            print("文件中最大日期为：%s" %(strMaxDate))
            checkStr = "发送错误邮件"
            for fileName in fileDict[strMaxDate]:
                #文件内容检索
                resultCode,count = fileProcess.readFiles(fileName,checkStr)
                if resultCode == 1:
                    errorMsg = "日志文件:"+fileName+"，第"+str(count)+"行出现处理异常！"
                    logResult.append(errorMsg)
            #判断处理结果是否为空，如果时空则不发送邮件，否则发送邮件
            #if len(logResult) != 0:
            resultCode = sendEmail.sendEmail(logResult)
    else :
        print("输入路径不正确，程序将退出！")

if __name__ == "__main__":
    main()
