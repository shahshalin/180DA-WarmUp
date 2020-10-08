#######
# REFERENCES
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html for template matching 
#######
import numpy as np
import cv2

cap = cv2.VideoCapture(1)
template = cv2.imread('fist.jpg',0)
method = eval('cv2.TM_SQDIFF_NORMED')#TM_CCORR_NORMED,TM_CCOEFF_NORMED
w, h = template.shape[::-1]
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    scale = 180 
    width = int(gray.shape[1] * scale / 100)
    height = int(gray.shape[0] * scale / 100)
    dim = (width, height)
    resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
    res = cv2.matchTemplate(resized,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc#max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(resized,top_left, bottom_right, 255, 2)
    cv2.imshow('frame',resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()