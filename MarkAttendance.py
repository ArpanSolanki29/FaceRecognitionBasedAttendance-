import mongo2
import DateTimeDetails

# Find The Subject
# create a dictionary

def Mark(Name, RollNo, Class):
    date, hour, minutes, day = DateTimeDetails.getDate()
    collection, db = mongo2.startConnection()
    # FIND CLASS_ID
    classID = mongo2.FindOne(RollNo, "Student", "ROLL_NO", "CLASS_ID")
    # FIND THE SUBJECT
    result = db["Table"].find_one({"CLASS_ID": classID, "DAY": day})
    # MAKING A DICTIONARY
    dict = {"AID": 1,
            "ROLL_NO": RollNo,
            "NAME": Name,
            "CLASS": Class,
            "DAY": day,
            "ATTENDED": result
    }

    mongo2.Insert(dict, "Attendance")
