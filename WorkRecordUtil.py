#File WorkRecodUtil.py
import sys;
import xlrd
from ExcelEntity import Person
# @author leijf elioray
# @time   2020/1/4
args = sys.argv;

sheetNum = 0
excelFilePath = ''
workrecordsheet = ''
personWorkTime = []
rowCount, colCount = 0,0
# 初始化输入的参数
def initlizeArgs(args):
    global sheetNum, excelFilePath
    # print(args)
    if len(args) < 3:
        print("输入参数有误")
        quit()
    sheetNum_input = args[2]
    excelFilePath_input = args[1]
    # print(excelFilePath_input)
    if sheetNum_input != 0:
        sheetNum = sheetNum_input
    if excelFilePath_input != '':
        excelFilePath = excelFilePath_input
        print(excelFilePath)

# 读取Excel文件
def readWorkBook(filePath):
    global workrecordsheet, rowCount, colCount
    print("read excel file path:" + str(filePath))
    workbook = xlrd.open_workbook(filePath)
    workrecordsheet = workbook.sheets()[2]
    rowCount = workrecordsheet.nrows
    colCount = workrecordsheet.ncols;
    print(workrecordsheet.name);
    print(workrecordsheet.nrows);
# 读取全部员工的数据
def readStaffWorkRecord():
    for i in range(1, rowCount - 1):
        rowData = workrecordsheet.row_values(i)
        for j in range(0, colCount):
            #print(rowData)
            col = rowData[j]
            #print(col)
            if(isinstance(col, float)):
                continue
            elif(col.find("姓") >= 0):
            # print(rowData[j + 2])
                i = i+1
                workTime = addworkTime(i)
                entity = Person(rowData[j + 2], workTime)
                personWorkTime.append(entity)
# 分析一个人工作时间
def addworkTime(rowNum):
    workTime = [];
    rowData = workrecordsheet.row_values(rowNum)
    for i in range(0, len(rowData)):
        dailyTime = rowData[i]
       # print(dailyTime.split("\n"))
        rideDupliate = list(set(dailyTime.split("\n")))
        rideDupliate.sort(key=dailyTime.index)
        workTime.append(rideDupliate)
    # print(workTime)
    return workTime

# 分析最后的结果
def analysis(personlist):
    for i in range(0, len(personlist)):
        person = personlist[i]
        recod = person.getRecord()
        #print(recod)
        for j in range(0, len(recod)):
            dayliRecord = recod[j]
            if len(dayliRecord)> 1 and len(dayliRecord) < 5 :
                print(person.get_name() +  str(j + 1)  + "号考勤异常")
        #person.printLate()

initlizeArgs(args)
readWorkBook(excelFilePath)
readStaffWorkRecord()
analysis(personWorkTime)