########
# REFERENCES AND RESEARCH 
# https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html
# https://www.youtube.com/watch?v=SJCu1d4xakQ
# got values for BGR + HSV experimentally AND with help from http://colorizer.org/ to pick the colors
# got help from https://github.com/PyXploiter/Barcode-Detection-and-Decoding/issues/2 for the findContours function
########
import cv2 
import numpy as np
import time
cap = cv2.VideoCapture(0) # front camera
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # trying to get 720p because sometimes regular doesn't work 
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) #1080p does not work -- too big for screen 
HSV = 1
if HSV:
    while(1): 
        res, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #print(hsv)
        #print(hsv[0].shape)
        #time.sleep(2)
        #print(hsv)
        lower = np.array([80, 100, 85]) # got values from http://colorizer.org/
        upper = np.array([100,255,255]) # got values from http://colorizer.org/
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        contours, _ = cv2.findContours(mask.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
        print(contours)
        if contours:
            joycon = sorted(contours, key=cv2.contourArea)
            joycon = joycon[-1] # joycon[0] gave trouble
            (x1,y1,x2,y2) = cv2.boundingRect(joycon)
            cv2.rectangle(frame,(x1,y1),(x1+x2, y1+y2),(0,255,0),2)
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
else:
    while(1): 
        res, frame = cap.read()
        bgr = frame.copy() #bgr by default
        lower = np.array([175, 140, 0]) # got values from http://colorizer.org/
        upper = np.array([230,175,80]) # got values from http://colorizer.org/
        mask = cv2.inRange(bgr, lower, upper)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        contours, _ = cv2.findContours(mask.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
        print(contours)
        if contours:
            joycon = sorted(contours, key=cv2.contourArea)
            joycon = joycon[-1] # joycon[0] gave trouble
            (x1,y1,x2,y2) = cv2.boundingRect(joycon)
            cv2.rectangle(frame,(x1,y1),(x1+x2, y1+y2),(0,255,0),2)
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
cv2.destroyAllWindows()