import numpy as np
import cv2
import timeit

start_time = timeit.default_timer()

img = cv2.imread('test5.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)
cv2.imshow('thresh',thresh)
_,contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print len(approx)
    if len(approx)==5:
        print "pentagon"
        cv2.drawContours(img,[cnt],0,255,5)
    elif len(approx)==3:
        print "triangle"
        cv2.drawContours(img,[cnt],0,(0,255,0),5)
    elif len(approx)==4:
        print "square"
        cv2.drawContours(img,[cnt],0,(0,0,255),5)
    elif len(approx) == 6:
        print "hexagon"
        cv2.drawContours(img,[cnt],0,(255,255,0),5)
    elif len(approx) > 15:
        print "circle"
        cv2.drawContours(img,[cnt],0,(0,255,255),5)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
