import cv2 as cv
import numpy as np

img=cv.imread("siddi.jpg")
img=cv.resize(img,(500,500))

m = cv.getRotationMatrix2D((250,250),90,1)
new_img=cv.warpAffine(img,m,(500,500))

h=np.hstack((img,new_img))
cv.imshow("Ram",h)
cv.waitKey(0)
cv.destroyAllWindows()