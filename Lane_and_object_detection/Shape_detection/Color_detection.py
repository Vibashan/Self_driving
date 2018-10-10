import cv2
import numpy as np
import timeit

def Color():
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	lower_red = np.array([0,120,160],np.uint8)
	upper_red  = np.array([20,255,255],np.uint8)
   
	lower_blue = np.array([83,120,120],np.uint8)
	upper_blue = np.array([170,255,255],np.uint8)

	lower_green = np.array([50,120,120],np.uint8)
	upper_green = np.array([80,255,255],np.uint8)

	red=cv2.inRange(hsv,lower_red , upper_red )
	blue=cv2.inRange(hsv, lower_blue, upper_blue)
	green=cv2.inRange(hsv, lower_green, upper_green)
	cv2.imshow("Color Tracking",img)
	cv2.imshow('red',red)
	cv2.imshow('blue',blue)
	cv2.imshow('green',green)
	return

start_time = timeit.default_timer()

img = cv2.imread('test5.png')

Color()

elapsed = timeit.default_timer() - start_time
print elapsed

cv2.waitKey(0)
cv2.destroyAllWindows()
