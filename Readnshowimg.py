import cv2 as cv

img=cv.imread("siddi.jpg")
cv.imshow("Siddi",img)
cv.imshow("Siddi2",img)
cv.waitKey(0)
cv.destroyAllWindows