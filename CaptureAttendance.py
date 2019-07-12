import cv2
import argparse
import Predict

cam = cv2.VideoCapture(0)


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

path = "C:/Users/arpan/Desktop/kaggle_dogs_vs_cats/test"

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
        netPath = path + "/" + "test" +".jpg"
        cv2.imwrite(netPath, image)
        Predict.predict(netPath)
        print("{} written!".format(netPath))


cam.release()
cv2.destroyAllWindows()
