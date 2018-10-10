import cv2
import numpy as np

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')
img4 = cv2.imread('4.jpg')
img5 = cv2.imread('5.jpg')
img6 = cv2.imread('6.jpg')

cv2.imshow('real',img1)

img1 = cv2.flip(img1,1)
cv2.imshow('flip',img1)


cv2.waitKey(0)
cv2.destroyAllWindows()