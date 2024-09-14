import cv2 as cv

cap=cv.VideoCapture("hi.mp4")

while cap.isOpened():
    r,frame=cap.read()
    if r == True:
        frame=cv.resize(frame,(500,500))
        cv.imshow("Ram",frame)
        if cv.waitKey(25) and 0xff==ord("p"):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()