

class Person:
    starTime = ['7:00', '1:00']
    endTime  = ['11:30', '17:00']
    recordPoints   = []
    def __init__(self, personname ,workRecord):
        self.personname = personname
        self.workRecord = workRecord
    # 打印考勤异常信息
    def getRecord(self):
        return self.workRecord;
    def get_name(self):
        return self.personname;

    def compareTime(firstTIme, secondTime):
        return False
    def printLate(self):
        recordPoints = ['7:00', '1:00','11:30', '17:00']
        for i in range(1, len(self.workRecord)):
            dailyTime = self.workRecord[i]
            if len(dailyTime) >= 5:
                recordPoint = 0
                for j in range(0,len(dailyTime)):
                    recodTime = dailyTime[j]
                    if recordPoint == 0:
                        if self.compareTime(recodTime,recordPoints[recordPoint]):
                            print(self.get_name() + str(i) + '早上迟到')
                            recordPoint = recordPoint + 1
                    if recordPoint == 1:   
                        if self.compareTime(recodTime,recordPoints[recordPoint]):
                            print(self.get_name() + str(i) + '中午早退')
                            recordPoint = recordPoint + 1
                    if recordPoint == 1:   
                        if self.compareTime(recodTime,recordPoints[recordPoint]):
                            print(self.get_name() + str(i) + '中午早退')
                            recordPoint = recordPoint + 1
                        # if case == 1:
                        
                        # if case == 2:

                        # if case == 4:
                    # 记录地一个下班时间 是否早退
                    # 记录第二上班时间是 是否迟到
                    # 记录第二个下班时间 是否早退

    def compareTime(self,firstTIme, secondTime):
        return True
