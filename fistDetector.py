import numpy as np
import cv2

cap = cv2.VideoCapture(0)
template = cv2.imread('fist.jpg',0)
method = eval('cv2.TM_SQDIFF_NORMED')#TM_CCORR_NORMED,TM_CCOEFF_NORMED
w, h = template.shape[::-1]
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    scale = 180 
    width = int(gray.shape[1] * scale / 100)
    height = int(gray.shape[0] * scale / 100)
    dim = (width, height)
    resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

    res = cv2.matchTemplate(resized,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    top_left = min_loc#max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(resized,top_left, bottom_right, 255, 2)

    # Display the resulting frame
    cv2.imshow('frame',resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()