import cv2 as cv

img=cv.imread("ramu.jpg")
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
 
cv.imshow(",",img)
cv.waitKey(0)
cv.destroyAllWindows()