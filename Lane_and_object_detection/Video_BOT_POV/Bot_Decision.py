#!/usr/bin/env python

import numpy as np
import cv2
import time

cap = cv2.VideoCapture('output3.avi')

while(1):
	ret, frame = cap.read()
	resize_img=cv2.resize(frame,(600,600))
	crop_img=resize_img[200:600,0:600]

	gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
	kernal= np.ones((5,5) , np.float32)/25
	median=cv2.medianBlur(gray, 25)
	ret,thresh = cv2.threshold(median,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	_,contours, h = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	sort=sorted(contours, key=cv2.contourArea, reverse=True)
	L1=sort[0]
	L2=sort[1]

	M1 = cv2.moments(L1)
	cx1 = int(M1['m10']/M1['m00'])
	cy1 = int(M1['m01']/M1['m00'])
	M2 = cv2.moments(L2)
	cx2 = int(M2['m10']/M2['m00'])
	cy2 = int(M2['m01']/M2['m00'])

	cx=(cx1+cx2)/2

	if(0<cx<310):
        	print "RIGHT"
    	elif(370<cx<600):
        	print "LEFT"
    	else:
        	print "STRAIGHT"

	cv2.circle(crop_img,(cx1,cy1),2,(255,0,0),4)
	cv2.circle(crop_img,(cx2,cy2),2,(255,0,0),4)

	cv2.imshow('frame',frame)
	#cv2.imshow('frame1',thresh)
	#cv2.imshow('frame',crop_img)
	
	time.sleep(0.2)

cap.release()
cv2.destroyAllWindows()
