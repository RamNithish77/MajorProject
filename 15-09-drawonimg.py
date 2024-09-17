import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype="uint8")

img = cv.imread("ramu.jpg")
blank[200:300,300:400]=0,255,0
cv.imshow(".",blank)
cv.waitKey(0)
cv.destroyAllWindows()