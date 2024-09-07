import cv2 as cv
import numpy as np

img=cv.imread(r"D:\py\siddi.jpg")
img=cv.resize(img,(400,400))

text="siddi"
org=(50,100)

txt=cv.putText(img=img,text=text,org=org,fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=3,color=(0,0,255),thickness=4,lineType=cv.ACCESS_MASK,bottomLeftOrigin=False)

txt=cv.putText(img=img,text=text,org=org,fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=3,color=(0,0,255),thickness=4,lineType=cv.ACCESS_MASK,bottomLeftOrigin=True)

cv.imshow("Ram",img)
cv.waitKey(0)
cv.destroyAllWindows
