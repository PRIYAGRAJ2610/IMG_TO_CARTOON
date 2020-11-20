#IMPORTING THE REQUIRED MODULES
import cv2
import numpy as np
img = cv2.imread('ViratKohli.JPG')

# RESIZING THE IMAGE ACCORDINGLY
img = cv2.resize(img,(650,750))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

#CARTOONING THE GIVEN IMAGE
color = cv2.bilateralFilter(img,9,250,250)
cartoon = cv2.bitwise_and(color,color,mask = edges)

#TO SHOW THE REAL IMAGE
cv2.imshow("image",img)

#TO SHOW THE CARTOON OF IMAGE
cv2.imshow("cartoon",cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()