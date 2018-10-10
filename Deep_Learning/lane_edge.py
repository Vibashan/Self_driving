#!/usr/bin/env python

import cv2
import numpy as np
import math
import time
import matplotlib.pyplot as plt

d = 0
cap=cv2.VideoCapture("training1.mp4")
plt.ion()

while(cap.isOpened()):
    ret, frame = cap.read()
    #frame = cv2.resize(frame,(640,480))
    image=frame[220:270,0:640]

    image = cv2.resize(image,(640,140))

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    median=cv2.GaussianBlur(gray,(1,1),0)
    
    edges = cv2.Canny(median,80,200)

    cv2.imshow("edges",edges)
    cv2.imshow("image",frame)
    filename = "edge8_%d.jpg"%d
    #cv2.imwrite(filename, edges)
    d+=1
    time.sleep(0.02)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

plt.close('all')
cap.release()
cv2.destroyAllWindows()
