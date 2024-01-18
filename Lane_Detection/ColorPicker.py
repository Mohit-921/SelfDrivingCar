# This script gives the value of HSV to be set in order to track the white path specifically

import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def empty():
    pass


cv2.namedWindow("HSV_settings")  # naming the window of our trackbars
cv2.resizeWindow("HSV_settings", 640, 240)
# cv.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)
cv2.createTrackbar("HUE Min", "HSV_settings", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV_settings", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV_settings", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV_settings", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV_settings", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV_settings", 255, 255, empty)

cap = cv2.VideoCapture('vid1.mp4')
# to capture video: use videocapture() then in an infinite loop, use read()
frameCounter = 0

while True:
    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0

    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "HSV_settings")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV_settings")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV_settings")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV_settings")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV_settings")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV_settings")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
