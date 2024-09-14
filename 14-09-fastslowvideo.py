import cv2 as cv

video=cv.VideoCapture("hi.mp4")
while video.isOpened:
    r,frame=video.read()
    if r:
        frame=cv.resize(frame,(600,600))
        cv.imshow("ram",frame)
        if cv.waitKey(5) & 0xff == ord("p"):
            #small number for fast video
            #big number for slow video
            break
    else:
        break
video.release()
cv.destroyAllWindows()