import os
import datetime
import time

def readPathFiles(pathName):
    nowDate = datetime.datetime.now()
    print("当前时间为： %s" %(datetime.datetime.strftime(nowDate,"%Y-%m-%d")))
    
    if len(pathName) != 0:
        #采用os.walk递归遍历文件夹
        #pathObjects = os.walk(pathName)
        #for root,dirs,files in pathObjects:
        #    for path in dirs :
        #        print("Path is %s " %(path))
        #    for file in files :
        #        print("File is %s" %(file))
        #初始化相关变量
        #maxFileDate : 文件最大的修改日期
        #fileDict    : 字典，key:日期,value:数组，记录文件名称
        maxFileDate = datetime.datetime.strptime("2019-01-01","%Y-%m-%d")
        fileDict = {}
        #print("初始化最大文件日期为：%s" %(datetime.datetime.strftime(maxFileDate,"%Y-%m-%d")))
        #获取特定的路径，这里通常为日志文件的目录
        fileLists = os.listdir(pathName)
        #遍历文件清单
        for fileName in fileLists:
            filePath = pathName + '/' + fileName
            #判断路径中，是否是文件
            if os.path.isfile(filePath) == True:
                #获取文件时间戳
                fileUpdateStamp = os.path.getmtime(filePath)
                #将时间戳转换成时间类型变量
                fileUpdateDate = datetime.datetime.fromtimestamp(fileUpdateStamp)
                #将时间转换成字符串，用于文本输出
                strFileUpdate = datetime.datetime.strftime(fileUpdateDate,"%Y-%m-%d")
                #获取最大文件的时间
                if fileUpdateDate >= maxFileDate :
                    maxFileDate = fileUpdateDate 
                #把日期添加到keys,把文件名添加到values
                if strFileUpdate not in fileDict.keys():
                    fileDict[strFileUpdate] = [filePath]
                else :
                    if fileName not in fileDict[strFileUpdate] :
                        fileDict[strFileUpdate].append(filePath)

                print("路径下文件信息:%s %s" %(filePath,datetime.datetime.strftime(fileUpdateDate,"%Y-%m-%d")))

        #print(fileDict)
        #print("最大时间日期：%s" %(datetime.datetime.strftime(maxFileDate,"%Y-%m-%d")))       
        return fileDict,maxFileDate
    else :       
        print("Cannot find the path , please ensure it correct.")
        return 
