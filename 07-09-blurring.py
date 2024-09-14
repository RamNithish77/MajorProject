import cv2 as cv
import numpy as np

img=cv.imread("siddi.jpg")
img=cv.resize(img,(500,500))

G_img=cv.GaussianBlur(img,(9,9),0)
m_img=cv.medianBlur(img,5)
b_img=cv.bilateralFilter(img,10,100,100)

Final_img=np.hstack((img,G_img,m_img,b_img))
cv.imshow("Ram",Final_img)
cv.waitKey(0)
cv.destroyAllWindows()