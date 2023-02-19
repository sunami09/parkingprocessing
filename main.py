import cv2
import cvzone
import time
import pickle
import numpy as np

print("Hi! I'm Mr. Parker. Choose one of the facilities you are visiting today?")
print("1. Costco")
print("2. Trader Joes")
print("3. Stanford Shopping Center")
print("Type the name of the facilities.")
k = str(input(">> "))
k = k.lower()
p = True

if k == "costco":
    key = 600
    video = "3.mp4"
    width, height = 107,47
    cordinates = "CarParkPos3"
elif k == "trader joes":
    key = 500
    video = "5.mp4"
    width, height = 83, 38
    cordinates = "CarParkPos5"
elif k == "stanford shopping center":
    key = 900
    video = "carPark.mp4"
    width, height = 107,47
    cordinates = "CarParkPos"
else:
    p = False
    print("Sorry! we don't offer our services at " + k)

if p != False:
    cap = cv2.VideoCapture(video)
    with open(cordinates, 'rb') as f:
        posList = pickle.load(f)
    
    def checkParkingSpace(imgPro):
        spaceCounter = 0

        for pos in posList:
            x, y = pos

            imgCrop = imgPro[y:y + height, x:x + width]
        
            count = cv2.countNonZero(imgCrop)


            if count < key:
                color = (0, 255, 0)
                thickness = 2
                spaceCounter += 1
            else:
                color = (0, 0, 255)
                thickness = 2

            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
            cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,thickness=2, offset=0, colorR=color)

        cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (400, 50), scale=2,
                            thickness=3, offset=20, colorR=(0,200,0))

    while True:

        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        success, img = cap.read()
        if k == "trader joes":
            img = cv2.resize(img, (583, 700))
        elif k == "costco":
            img = cv2.resize(img, (750, 750))
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        checkParkingSpace(imgDilate)
        cv2.imshow("Image", img)
        cv2.waitKey(10)



