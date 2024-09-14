import cv2 as cv

cap=cv.VideoCapture(0)
while True:
    r,frame=cap.read()
    if r:
        frame=cv.resize(frame,(600,600))
        cv.imshow("ram",frame)
        if cv.waitKey(25) & 0xff == ord("p"):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()