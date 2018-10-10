import  cv2
import numpy as np
import math 

x1 = 9
x2 = 545
y  = 285
h  = -28
Ot = math.radians(55)

a = x1 + (h/math.tan(Ot))
b = x2 - (h/math.tan(Ot))

img = cv2.imread('img1.jpg',1)
resized_img = cv2.resize(img,(600,600))

#                  [0,0]   [600,0] [0,600][600,600]
pts1 = np.float32([[a,y+h],[b,y+h],[x1,y],[x2,y]])
pts2 = np.float32([[0,0],[600,0],[0,600],[600,600]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(resized_img,M,(600,600))

cv2.imshow('img',resized_img)
cv2.imshow('dst',dst)

cv2.waitKey(0)