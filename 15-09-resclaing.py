import cv2 as cv

def set_resolution(cap, width, height):
    # Set the resolution of the capture
    cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)

cap = cv.VideoCapture(0)

# Set resolution to 640x480
set_resolution(cap, 1000, 600)

while cap.isOpened():
    r, frame = cap.read()
    if r:
        cv.imshow("Ram", frame)
        if cv.waitKey(25) & 0xFF == ord('p'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
