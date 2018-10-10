import cv2
import numpy as np
import timeit

start_time = timeit.default_timer()
def Shape():	
 for cnt in contours:
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    if len(approx)==3:
        cv2.putText(img,"Triangle %s (%d,%d)"%(color,cx,cy),(cx,cy),0,0.4,(0,0,0),1,16)
    elif len(approx)==4:
	pts = np.array([approx[0], approx[1], approx[2],approx[3]]) 
	x = pts[[0,1,2,3], [0,0,0,0],[0,0,0,0]]
	y = pts[[0,1,2,3], [0,0,0,0],[1,1,1,1]]
	m1=(y[2]-y[0])/(x[2]-x[0])
	m2=(y[3]-y[1])/(x[3]-x[1])
	m=m1*m2
	if m==-1:
		cv2.putText(img,"Rhombus %s (%d,%d)"%(color,cx,cy),(cx,cy),0,0.4,(0,0,0),1,16)
	else:
		cv2.putText(img,"Trapizium %s (%d,%d)"%(color,cx,cy),(cx,cy),0,0.4,(0,0,0),1,16)
    elif len(approx)==5:
        cv2.putText(img,"Pentagon %s (%d,%d)"%(color,cx,cy),(cx,cy),0,0.4,(0,0,0),1,16)
    elif len(approx) == 6:
        cv2.putText(img,"Hexagon %s (%d,%d)"%(color,cx,cy),(cx,cy),0,0.4,(0,0,0),1,16)
    elif len(approx) > 15:
        cv2.putText(img,"Circle %s (%d,%d)"%(color,cx,cy),(cx,cy),0,0.4,(0,0,0),1,16)
 return img

img = cv2.imread('test5.png')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([0,120,160],np.uint8)
upper_red  = np.array([20,255,255],np.uint8)
red=cv2.inRange(hsv,lower_red , upper_red )
_,contours,h = cv2.findContours(red,1,2)
color="Red"
img=Shape()
   
lower_blue = np.array([83,120,120],np.uint8)
upper_blue = np.array([170,255,255],np.uint8)
blue=cv2.inRange(hsv, lower_blue, upper_blue)
_,contours,h = cv2.findContours(blue,1,2)
color="Blue"
img=Shape()

lower_green = np.array([50,120,120],np.uint8)
upper_green = np.array([80,255,255],np.uint8)
green=cv2.inRange(hsv, lower_green, upper_green)
_,contours,h = cv2.findContours(green,1,2)
color="Green"
img=Shape()

cv2.imshow("Color Tracking",img)

elapsed = timeit.default_timer() - start_time
print elapsed

cv2.waitKey(0)
cv2.destroyAllWindows()
