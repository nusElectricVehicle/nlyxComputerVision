#Detecting colors (Hsv Color Space) - Opencv with Python
#https://www.youtube.com/watch?v=Q0IPYlIK-4A
#YouTube by Pysource

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #_ only gives the value True but you have to extract it
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    #Red Color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    '''
    #Blue Color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask = blue_mask)


    #Green Color
    low_green = np.array([94, 80, 2])
    high_green = np.array([126, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask = green_mask)

    '''

    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])

    #cv2.imshow("Frame", frame)
    cv2.imshow("Red mask", red)

    key = cv2.waitKey(1)
    if key == 27:
        break
