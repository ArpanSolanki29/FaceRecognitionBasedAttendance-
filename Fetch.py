import mongo2
import pymongo
import datetime

def FetchName(RollNo):
    print("[INFO] getting access to Student database")
    result = mongo2.FindOne(RollNo, "Student", "ROLL_NO", "NAME")
    print(result)
    return result



def FetchClass(ROLLNO):
    print("[INFO] getting access to Class database")
    classID = mongo2.FindOne(ROLLNO, "Student", "ROLL_NO", "CLASS_ID")
    print(classID)
    className = mongo2.FindOne(int(classID), "Class", "CLASS_ID", "CLASS")
    print(className)
    return className


#NOTE: find() method returns a cursor