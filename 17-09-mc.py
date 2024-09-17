import cv2 as cv
from mtcnn import MTCNN

detector = MTCNN()

cap = cv.VideoCapture(0)

while cap.isOpened():
    r, frame = cap.read()
    if r:
        frame = cv.resize(frame,(300,300))
        
        # Convert frame to RGB for MTCNN
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        # Detect faces
        detections = detector.detect_faces(rgb_frame)
        
        # Draw rectangles around detected faces
        for detection in detections:
            x, y, w, h = detection['box']
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        cv.imshow("Face Detection", frame)
        
        if cv.waitKey(25) & 0xFF == ord('p'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
