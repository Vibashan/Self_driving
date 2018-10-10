import numpy as np
import cv2
import math
import timeit

a="red"

def Shape():
 #_,contours,h = cv2.findContours(thresh,1,2)
 for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    if len(approx)==3:
	#print cx
	#print cy
	start_time = timeit.default_timer()
        cv2.putText(img,"Triangle %s (%d,%d)"%(a,cx,cy),(cx,cy), cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),1,cv2.LINE_AA)
	elapsed = timeit.default_timer() - start_time
	print elapsed
    elif len(approx)==4:
	pts = np.array([approx[0], approx[1], approx[2],approx[3]]) 
	x = pts[[0,1,2,3], [0,0,0,0],[0,0,0,0]]
	y = pts[[0,1,2,3], [0,0,0,0],[1,1,1,1]]
	m1=(y[2]-y[0])/(x[2]-x[0])
	m2=(y[3]-y[1])/(x[3]-x[1])
	m=m1*m2
	#print m
    elif len(approx)==5:
        print "pentagon"
    elif len(approx) == 6:
        print "hexagon"
    elif len(approx) > 15:
        print "circle"
    return 



img = cv2.imread('test5.png')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_green = np.array([50,120,120],np.uint8)
upper_green = np.array([80,255,255],np.uint8)
green=cv2.inRange(hsv, lower_green, upper_green)
_,contours,h = cv2.findContours(green,1,2)
color="Green"
img=Shape()
   
#cv2.imshow('thresh',thresh)

#Shape()



#cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
