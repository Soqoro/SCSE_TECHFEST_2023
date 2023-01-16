import cv2
import pickle

#width and height of the carpark detection boxes 
width, height = 88,43

# 
try:
    with open('CarParkPos2', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
 
#function of mouseClick to create detection boxes 
def mouseClick(events, x, y, flags, params):
    #left click function to add new boxes
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    
    #right click function to delete
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    
    #open binary storage
    with open('CarParkPos2', 'wb') as f:
        pickle.dump(posList, f)
for pos in posList:
    print(pos)

#run main programme to allow creating or deleting detection boxes
while True:
    img = cv2.imread('./images/parkinglot2.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)
    
