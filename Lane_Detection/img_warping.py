import cv2
import numpy as np

import temp2
import utlis

curveList = []
avgVal = 10

def getLaneCurve(img, display=2):
    imgCopy = img.copy()
    #### STEP 1
    imgThres = utlis.thresholding(img)

    #### STEP 2
    hT, wT, c = img.shape
    points = utlis.valTrackbars()
    imgWarp = utlis.warpImg(img, points, wT, hT)
    imgWarpPoints = utlis.drawPoints(imgCopy, points)

    ### step 3
    temp2.getHistogram(imgWarp)

    cv2.imshow('Thres',imgThres)
    cv2.imshow('Warped',imgWarp)
    cv2.imshow('Warp Points', imgWarpPoints)
    return None

if __name__ == '__main__':
    cap = cv2.VideoCapture('vid1.mp4')
    intialTrackBarVals = [100, 100, 100, 100]
    utlis.initializeTrackbars(intialTrackBarVals)
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0

        success, img = cap.read()
        img = cv2.resize(img, (480, 240))
        getLaneCurve(img)
        cv2.imshow('Vid',img)
        cv2.waitKey(10)