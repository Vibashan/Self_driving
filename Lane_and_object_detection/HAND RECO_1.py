import cv2
import numpy as np
import math
import serial
#ser=serial.Serial("COM4",9600)

cap = cv2.VideoCapture(-1)

while(cap.isOpened()):
    ret, img = cap.read()
    crop_img = img[90:320, 10:250]
    gray = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
    kernal= np.ones((5,5) , np.float32)/25
    
    blur = cv2.GaussianBlur(gray,(15,15),0)
    ret,thresh = cv2.threshold(blur,210,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    thresh1=cv2.medianBlur(thresh, 15)
    cv2.imshow('thresh1',thresh1)
    
    _,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros(crop_img.shape,np.uint8)

    max_area=0
   
    for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
    cnt=contours[ci]
    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)
    if moments['m00']!=0:
                cx = int(moments['m10']/moments['m00']) # cx = M10/M00
                cy = int(moments['m01']/moments['m00']) # cy = M01/M00
              
    centr=(cx,cy)       
    cv2.circle(crop_img,centr,5,[0,0,255],2)       
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2) 
    cv2.drawContours(drawing,[hull],0,(0,0,255),2) 
    cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    hull = cv2.convexHull(cnt,returnPoints = False)
    
    defects = cv2.convexityDefects(cnt,hull)
    mind=0
    maxd=0
    for i in range(defects.shape[0]):
                    s,e,f,d = defects[i,0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])
                    cv2.line(img,start,end,[0,255,0],2)        
                    cv2.circle(img,far,5,[0,0,255],-1)
    print(i)
               #if  i>1:
             #   ser.write('1')
              # else:
           #      ser.write('0')
    i=0
    cv2.imshow('output',drawing)
    cv2.imshow('input',img)
                
    k = cv2.waitKey(10)
    if k == 27:
        break
