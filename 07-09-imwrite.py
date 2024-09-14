import cv2 as cv
import numpy as np

img=cv.imread("siddi.jpg")
img=cv.resize(img,(500,500))

h=np.hstack((img,img))
v=np.vstack((h,h))

cv.imshow("Ram",v)
cv.imwrite("new-siddi.png",v)
cv.waitKey(0)
cv.destroyAllWindows()