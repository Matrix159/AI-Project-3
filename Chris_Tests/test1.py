import numpy as np
import cv2
import pyautogui

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# For Fist: https://github.com/Aravindlivewire/Opencv/blob/master/haarcascade/aGest.xml
fist_cascade = cv2.CascadeClassifier('aGest.xml')
# For Palm: https://github.com/Aravindlivewire/Opencv/blob/master/haarcascade/palm.xml
palm_cascade = cv2.CascadeClassifier('palm.xml')

cap = cv2.VideoCapture(0)
click = 0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fist = fist_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in fist:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        if click == 1:
            print("click")
            pyautogui.click()
            click = 0

    palm = palm_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in palm:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        click = 1

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
