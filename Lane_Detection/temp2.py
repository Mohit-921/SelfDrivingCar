import numpy as np
import cv2

# img_read = cv2.imread('letterA.jpg', cv2.IMREAD_GRAYSCALE)


def printImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# print(f'Shape = {img_read.shape[0]}*{img_read.shape[1]} pixels')
def getHistogram(img, minPer=0.1, display=False):
    histValues = np.sum(img, axis=0)
    # print(f"Summation of all columns: {histValues}")

    maxValue = np.max(histValues)
    minValue = minPer * maxValue

    indexArray = np.where(histValues >= minValue)
    basePoint = int(np.average(indexArray))  # avg or middle of index_array

    if display:
        imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        cv2.imshow('before processing', img)
        for x, intensity in enumerate(histValues):  # x: index of histValues
            # cv2.line(imgHist, (x, img.shape[0]), (x, img.shape[0] - intensity // 255), (255, 0, 255), 1)
            cv2.circle(imgHist, (basePoint, img.shape[0]), 20, (0, 255, 255), cv2.FILLED)  # ****
        return basePoint, imgHist

    return 0, basePoint


# print(f'Shape = {img_read.shape[0]}*{img_read.shape[1]} pixels')
# _, img_hist = getHistogram(img_read, display=False)
# cv2.imshow('hsit', img_hist)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if __name__ == '__main__':
    cap = cv2.VideoCapture('vid1.mp4')
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0

        success, img = cap.read()
        img = cv2.resize(img, (480, 240))
        _, img_hist = getHistogram(img, display=False)
        printImage(img_hist)
