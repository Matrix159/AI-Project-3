import cv2
import numpy as np
import pyautogui
from collections import deque
import imutils

# region globals

max_buffer_size = 32

# Buffer of past points.
points = deque([],  max_buffer_size)

# Camera
camera = cv2.VideoCapture(0)

# Skin color thresholds in HSV
skinColorLower = (106, 28, 80)
skinColorUpper = (135, 167, 197)

# Skin color thresholds in YCrCb
YCrCb_Ymin = 0
YCrCb_Ymax = 255
YCrCb_crMin = 133
YCrCb_crMax = 173
YCrCb_cbMin = 77
YCrCb_cbMax = 127

# background subtractor
bs = cv2.createBackgroundSubtractorMOG2()



counter = 0

(dX, dY) = (0, 0)

direction = ""





# endregion


while True:
    (success, frame) = camera.read()

    # resize frame to increase processing speed
    frame = imutils.resize(frame, width=600)

    #blur to remove noise
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    # convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #convert frame to YCbCr
    ycbcr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

    cv2.imshow('ycbcr', ycbcr)

    #background subtractor
    #modFrame = bs.apply(frame)
    #cv2.imshow('frame', hsv)

    #filter for skin color in YcrCb color space
    modFrame = cv2.inRange(ycbcr, (YCrCb_Ymin, YCrCb_crMin, YCrCb_cbMin), (YCrCb_Ymax, YCrCb_crMax, YCrCb_cbMax))

    #eliminate distortions
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    #modFrame = cv2.erode(modFrame, kernel, iterations=1)
    modFrame = cv2.dilate(modFrame, None, iterations=1)
    modFrame = cv2.GaussianBlur(modFrame, (3, 3), 0)

    cv2.imshow('frame', modFrame)

    #Find contours
    #contours = cv2.findContours(modFrame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    #center = None

    #check to see if an object was detected
    #if len(contours) > 0:
        #largestContour = max(contours, key=cv2.contourArea)
        #((x,y), radius) = cv2.minEnclosingCircle(largestContour)

        #M = cv2.moments(largestContour)
        #center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        #if radius > 10:
            #cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            #cv2.circle(frame, center, 5, (0, 0, 255), -1)
            #points.appendleft(center)

        #cv2.circle(frame, center, 10, (255,50,0), thickness=1, lineType=None, shift=None)














    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

camera.release()
cv2.destroyAllWindows()