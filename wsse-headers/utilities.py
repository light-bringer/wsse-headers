import datetime

def gendate():
        curDate = datetime.datetime.now().replace(microsecond=0)
        return curDate.strftime('%Y%m%d%H%M%S')

