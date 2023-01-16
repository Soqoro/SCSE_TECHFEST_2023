import cv2
import pickle
import cvzone
import numpy as np
 
# Video feed
feed = cv2.VideoCapture('./videos/cropped.mp4')

#setting size of the boxes 
width, height = 88,43
 
with open('CarParkPos2', 'rb') as f:
    posList = pickle.load(f)


def checkParkingSpace(imgPro):
    emptySpace = 0
 
    for pos in posList:
        x, y = pos
 
        imgCrop = imgPro[y:y + height, x:x + width]
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)
 
        #detection criteria of empty lots, 200 pixels
        if count < 200:
            color = (80, 230, 0)
            thickness = 1
            emptySpace += 1
        else:
            color = (0, 0, 230)
            thickness = 1
 
        #create lot detection boxes
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        
        #count number of pixels within the box
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=0.6,
                           thickness=1, offset=0, colorR=color)
    
    #display total number of empty lots
    cvzone.putTextRect(img, f'Free: {emptySpace}/{len(posList)}', (150, 50), scale=2,
                           thickness=3, offset=20, colorR=(0,200,0))

#main function body to run live vidoe feed
while True:
    if feed.get(cv2.CAP_PROP_POS_FRAMES) == feed.get(cv2.CAP_PROP_FRAME_COUNT):
        feed.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = feed.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    kernel = np.ones((3, 3), np.uint8)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
 
    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    cv2.waitKey(10)