import mongo2

def Enter(day):
    collection, db = mongo2.startConnection()
    posts = db.Attendance
    post_data = {
        "AID": "1",
        "ROLL_NO": "19",
        "DAY": day
    }
    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))

