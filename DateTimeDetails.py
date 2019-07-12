import datetime
import mongo2

def getDate():
    currentTime = datetime.datetime.now()
    date = currentTime.date
    hour = currentTime.hour
    minutes = currentTime.minute
    day = currentTime.strftime("%A")
    print(day)
    return date, hour, minutes, day


