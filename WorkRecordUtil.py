
import sys;

args = sys.argv;

if(len(args) < 2):
    print("输入参数有误")
    exit

excelFilePath = args[1]
inputSheet = args[2]
defaultSheetNum = 2
