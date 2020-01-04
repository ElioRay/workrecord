
# author leijf
# time   2020/01/03
# DesC　　Excel文件操作类
import xlrd
import sys
from ExcelEntity import Person

print("接收参数" + str(sys.argv));
#　打开文件
workbook = xlrd.open_workbook("/home/elio/桌面/workbook.xls")

workrecordsheet = workbook.sheets()[2]

personWorkTime = []
rowCount = workrecordsheet.nrows
colCount = workrecordsheet.ncols;

print(workrecordsheet.name);
print(workrecordsheet.nrows);

def analysiz(personlist):
    for i in range(0, len(personlist)):
        person = personlist[i]
        recod = person.getRecord()
        #print(recod)
        for j in range(0, len(recod)):
            dayliRecord = recod[j]
            if len(dayliRecord)> 1 and len(dayliRecord) < 5 :
                print(person.get_name() +  str(j + 1)  + "号考勤异常")
        person.printLate()


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
for i in range(1, rowCount - 1):
    rowData = workrecordsheet.row_values(i)
    for j in range(0, colCount):
        #print(rowData)
        col = rowData[j]
        #print(col)
        if(isinstance(col, float)):
            print()
        elif(col.find("姓") >= 0):
           # print(rowData[j + 2])
            i = i+1
            workTime = addworkTime(i)
            entity = Person(rowData[j + 2], workTime)
            personWorkTime.append(entity)
        #print(col)
        
analysiz(personWorkTime)

