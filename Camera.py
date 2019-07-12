import cv2
import os
import argparse
import mongo2
import time




cam = cv2.VideoCapture(0)

arg = argparse.ArgumentParser()
arg.add_argument("-r", "--rollNumber", required=True, help="path to input dataset")
arg.add_argument("-n", "--Name", required=True, help="path to input dataset")
arg.add_argument("-c", "--ClassID", required=True, help="path to input dataset")



args = vars(arg.parse_args())

start = time.time()
print(start)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

path = "C:/Users/arpan/Desktop/kaggle_dogs_vs_cats/" + args["rollNumber"]
if not os.path.exists(path):
    os.makedirs(path)

image = 0
count = 0

while (True):
    ret, img = cam.read()
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(img, 1.3, 5)
    for (x, y, w, h) in faces:
        x1 = x
        y1 = y
        x2 = x + w
        y2 = y + h

        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
        # Save the captured image into the datasets folder
        image = img[y1:y2, x1:x2]
        cv2.imshow('image', img)

    k = cv2.waitKey(1) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif k == 32:
        # SPACE pressed
        count += 1
        img_name = "{}.png".format(count)
        cv2.imwrite(path + "/" + str(count) +".jpg", image)
        print("{} written!".format(img_name))

cam.release()
cv2.destroyAllWindows()


def Student_Dict():
    dict = {"ROLL_NO": args["rollNumber"],
            "NAME": args["Name"],
            "CLASS_ID": args["ClassID"],
            }
    mongo2.Insert(dict, "Student")

Student_Dict()

end = time.time()
print(end)
minutes, seconds = divmod(end-start, 60)
print(minutes)
print(seconds)
