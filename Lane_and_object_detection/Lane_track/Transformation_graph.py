import  cv2
import numpy as np

img=cv2.imread('track.jpg',1)
resized_img=cv2.resize(img,(600,600))

rows,cols,ch = resized_img.shape
pts1 = np.float32([[449,288],[552,375],[232,417],[340,546]])
pts2 = np.float32([[0,0],[600,0],[0,600],[600,600]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(resized_img,M,(600,600))

cv2.imshow('img',resized_img)
cv2.imshow('dst',dst)
cv2.imwrite('Lane_track.jpg',dst)

cv2.waitKey(0)
