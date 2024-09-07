import cv2 as cv
img=cv.imread(r"D:\py\siddi.jpg")
img=cv.resize(img,(500,500))

text="siddi"
org=(20,80)

txt=cv.putText(img=img,text=text,org=org,fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,0,255),thickness=4,lineType=cv.ACCESS_MASK,bottomLeftOrigin=False)
#--------------line-------------------
# img=cv.line(img=img,pt1=(170,100),pt2=(350,100),color=(0,255,0),thickness=4,lineType=4)
# cv.imshow("ram",img)
# cv.waitKey(0)
# cv.destroyAllWindows()
#-------------------------------------
img=cv.rectangle(img=img,pt1=(170,60),pt2=(350,250),color=(0,255,0),thickness=4,lineType=4)
cv.imshow("ram",img)
cv.waitKey(0)
cv.destroyAllWindows()
