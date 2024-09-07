import cv2 as cv
import cv2 as cv
siddi=cv.imread("siddi.jpg")
ramu=cv.imread("ramu.jpg")
gp1=cv.imread("gp.jpg")

siddi=cv.resize(siddi,(500,500))
ramu=cv.resize(ramu,(500,500))
gp=cv.resize(gp1,(500,500))


# img=cv.addWeighted(src1=ramu,alpha=1,src2=siddi,beta=0.5,gamma=1)

img=cv.subtract(gp,siddi)
cv.imshow("ram",img)
cv.waitKey(0)
cv.destroyAllWindows()