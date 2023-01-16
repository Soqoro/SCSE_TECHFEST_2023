def checkParkingSpace(imgPro):
    emptySpace = 0
 
    for pos in posList:
        x, y = pos
 
        imgCrop = imgPro[y:y + height, x:x + width]
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)
 
        #detection criteria of empty lots, 200 pixels
        if count < 900:
            color = (80, 230, 0)
            thickness = 1
            emptySpace += 1
        else:
            color = (0, 0, 230)
            thickness = 1
 