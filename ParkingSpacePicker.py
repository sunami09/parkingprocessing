
import cv2
import pickle # package to save all the positions of the parking spaces to then bring to the main code


width, height = 107,47
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)




while True:
    # cv2.rectangle(img, (50,287), (158,335),(255,0,255),2)
    img = cv2.imread('carParkImg.png')
    #img = cv2.resize(img, (583, 700))
    # img = cv2.resize(img, (750, 750))
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height),(255,0,255),2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)
