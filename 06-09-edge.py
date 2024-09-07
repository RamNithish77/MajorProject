import cv2 as cv
import numpy as np
 
siddi=cv.imread("siddi.jpg")
siddi=cv.resize(siddi,(500,500))
 
new_img=cv.Canny(image=siddi,threshold1=50,threshold2=50)

# img=np.hstack((siddi,new_img))

cv.imshow("ram",new_img)
cv.waitKey(0)
cv.destroyAllWindows()