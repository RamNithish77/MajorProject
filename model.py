import cv2
naruto = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
luffy = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
if naruto.empty() or luffy.empty():
    raise IOError("Failed to load cascade classifier xml file")
goku = cv2.VideoCapture(0)
while True:
    ret, frame = goku.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    baurto = naruto.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in baurto:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, 'Face Detected', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = luffy.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
goku.release()
cv2.destroyAllWindows()
