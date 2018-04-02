import numpy as np
import cv2
import pyautogui
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
hand = cv2.CascadeClassifier('testhand.xml')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    hands = hand.detectMultiScale(gray, 1.1, 5)

    for(x, y, w, h) in hands:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #pyautogui.moveTo(x, y)
    cv2.imshow('Frame', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()