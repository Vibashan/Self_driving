#!/usr/bin/env python

import cv2
import numpy as np
import math
import time
import matplotlib.pyplot as plt

cap=cv2.VideoCapture("output3.mp4")

x1 = 8
x2 = 550
y = 390
h = -30
Ot = math.radians(45)
a = x1 - (h / math.tan(Ot))
b = x2 + (h / math.tan(Ot))
plt.ion()


while(cap.isOpened()):
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    pts1 = np.float32([[a,y+h],[b,y+h],[x1,y],[x2,y]])
    pts2 = np.float32([[0,0],[640,0],[0,480],[640,480]])

    M=cv2.getPerspectiveTransform(pts1,pts2)
    dst=cv2.warpPerspective(gray,M,(640,480))
    pts=np.array([[a,y+h],[b,y+h],[x2,y],[x1,y]],np.int32)
    cv2.polylines(frame, [pts],True,(255,255,255),2)
    
    blur=cv2.GaussianBlur(dst,(3,3),0)
    ret,threshold=cv2.threshold(blur,,255,cv2.THRESH_BINARY_INV)
    kernel=np.ones((5,5),np.uint8)
    thresh=cv2.erode(threshold,kernel,iterations=3)
    thresh2=cv2.dilate(thresh,kernel,iterations=3)

    hist = np.sum(threshold, axis=0)
    np.reshape(hist, (-1, 1))
    #print hist

    n = np.arange(1, hist.shape[0] + 1, 1)
    n = n[:, np.newaxis]
    
    avg = np.average(hist)
    print avg
    plt.plot(n, hist)
    plt.show()
    plt.pause(0.0001)

    cv2.imshow("thresh",thresh2)
    #cv2.imshow("dst",dst)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

plt.close('all')
cap.release()
cv2.destroyAllWindows()
