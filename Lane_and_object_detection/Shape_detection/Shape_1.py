import numpy as np
import cv2

img = cv2.imread('all_three.png')
gray = cv2.imread('all_three.png',0)

_,thresh = cv2.threshold(gray,220,255,1)
cv2.imshow('img-0',thresh)
_,contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    print  len( approx)

cv2.imshow('img',thresh)
cv2.imshow('img_1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
