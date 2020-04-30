#create a function to load log files
def readFiles(fileName,checkStr):
    #数据处理结果：1:命中  0:未命中
    resultCode = 0
    count = 0
    if len(fileName) != 0:
        #打开文件读行
        fileData = open(fileName,encoding="GB2312").readlines()
        for rows in fileData:
            count += 1
            #find：匹配不到数据，返回-1
            if rows.find(checkStr,0) != -1:
                resultCode = 1
                exit
    return resultCode,count
        


