import cv2 as cv
import numpy as np
import os

# img=cv.imread("siddi.jpg")
# img=cv.resize(img,(400,400))

# h=np.hstack((img,img))#adds horizontally
# v=np.vstack((h,h))#adds vertically

# cv.imshow("Siddi2",v)
# cv.waitKey(0)
# cv.destroyAllWindows

list_anime=os.listdir(r"D:\py\images")
print(list_anime)

for i in list_anime:
    path="D:\\py\\images"
    images_path=path+"\\"+i
    img=cv.imread(images_path)
    img_re=cv.resize(img,(500,500))
    cv.imshow("Ram",img_re)
    cv.waitKey(3000)
cv.destroyAllWindows
