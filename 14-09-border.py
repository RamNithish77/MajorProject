import cv2 as cv
import numpy as np

img=cv.imread("ramu.jpg")
img=cv.resize(img,(500,500))

new_img=cv.copyMakeBorder(img,20,20,20,20,cv.BORDER_CONSTANT,None,value=2)
new_img=cv.resize(new_img,(500,500))

f_img=np.hstack((img,new_img))
cv.imshow("ram",f_img)
cv.waitKey(0)
cv.destroyAllWindows()