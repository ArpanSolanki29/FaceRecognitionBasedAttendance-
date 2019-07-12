# USAGE
# python knn_classifier.py --dataset kaggle_dogs_vs_cats

# import the necessary packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from imutils import paths
import numpy as np
import imutils
import cv2
import os
import sys

import Fetch
import MarkAttendance

sys.path.insert(0, "C:/Users/arpan/Desktop/New folder (2)")


def image_to_feature_vector(image, size=(32, 32)):
    # resize the image to a fixed size, then flatten the image into
    # a list of raw pixel intensities
    return cv2.resize(image, size).flatten()

def extract_color_histogram(image, bins=(8, 8, 8)):
    # extract a 3D color histogram from the HSV color space using
    # the supplied number of `bins` per channel
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1, 2], None, bins,
        [0, 180, 0, 256, 0, 256])

    # handle normalizing the histogram if we are using OpenCV 2.4.X
    if imutils.is_cv2():
        hist = cv2.normalize(hist)

    # otherwise, perform "in place" normalization in OpenCV 3 (I
    # personally hate the way this is done
    else:
        cv2.normalize(hist, hist)

    # return the flattened histogram as the feature vector
    return hist.flatten()


def predict(testpath):
    # grab the list of images that we'll be describing

    path = "C:/Users/arpan/Desktop/kaggle_dogs_vs_cats"
    print("[INFO] describing images...")
    imagePaths = list(paths.list_images(path))

    print("This is imagepaths")
    print(imagePaths)

    rawImages = []
    features = []
    labels = []

    imgloc = testpath
    image = cv2.imread(imgloc)
    image = image_to_feature_vector(image)
    print("This is image")
    print(image)



    image = np.array(image)
    print("image")
    print(image.shape)

    # loop over the input images
    for (i, imagePath) in enumerate(imagePaths):
        # load the image and extract the class label (assuming that our
        # path as the format: /path/to/dataset/{class}.{image_num}.jpg
        image = cv2.imread(imagePath)
        label = imagePath.split(os.path.sep)[-2]

        # extract raw pixel intensity "features", followed by a color
        # histogram to characterize the color distribution of the pixels
        # in the image
        pixels = image_to_feature_vector(image)
        hist = extract_color_histogram(image)
        pixels.reshape(1, -1)

        # update the raw images, features, and labels matricies,
        # respectively
        rawImages.append(pixels)
        features.append(hist)
        labels.append(label)

        # show an update every 1,000 images
        if i > 0 and i % 1000 == 0:
            print("[INFO] processed {}/{}".format(i, len(imagePaths)))

    # show some information on the memory consumed by the raw images
    # matrix and features matrix
    rawImages = np.array(rawImages)
    features = np.array(features)
    labels = np.array(labels)

    print(labels)

    print(rawImages[0].shape)

    print("[INFO] pixels matrix: {:.2f}MB".format(
        rawImages.nbytes / (1024 * 1000.0)))
    print("[INFO] features matrix: {:.2f}MB".format(
        features.nbytes / (1024 * 1000.0)))

    # partition the data into training and testing splits, using 75%
    # of the data for training and the remaining 25% for testing
    (trainRI, testRI, trainRL, testRL) = train_test_split(
        rawImages, labels, test_size=0.25, random_state=42)
    (trainFeat, testFeat, trainLabels, testLabels) = train_test_split(
        features, labels, test_size=0.25, random_state=42)

    # train and evaluate a k-NN classifer on the raw pixel intensities
    print("[INFO] evaluating raw pixel accuracy...")
    model = KNeighborsClassifier(n_neighbors=3,
                                 n_jobs=1)
    model.fit(trainRI, trainRL)
    acc = model.score(testRI, testRL)
    print("[INFO] raw pixel accuracy: {:.2f}%".format(acc * 100))

    # train and evaluate a k-NN classifer on the histogram
    # representations
    print("[INFO] evaluating histogram accuracy...")
    model = KNeighborsClassifier(n_neighbors=3,
                                 n_jobs=1)
    model.fit(trainFeat, trainLabels)
    acc = model.score(testFeat, testLabels)
    print("[INFO] histogram accuracy: {:.2f}%".format(acc * 100))

    imgloc = testpath
    image = cv2.imread(imgloc)
    image = extract_color_histogram(image)
    image = image.reshape(1, -1)
    print("This is image")
    print(image.shape)
    print(testRI.shape)

    prediction = model.predict(image)
    print("this is prediction")
    print(int(prediction[0]))

    Name = Fetch.FetchName(prediction[0])
    print(Name)
    Class = Fetch.FetchClass(prediction[0])
    print(Class)
    print("LINE 150")
    MarkAttendance.Mark(Name, prediction[0], Class)

    os.remove("C:/Users/arpan/Desktop/kaggle_dogs_vs_cats/test/test.jpg")


    #date, hour, minutes, day = DateTimeDetails.getDate()

    #EnterAttendance.Enter(day)
    #mongo2.posting(str(prediction[0]))