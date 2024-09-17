import cv2 as cv
import numpy as np

net = cv.dnn.readNetFromCaffe(
    'deploy.prototxt', 
    'res10_300x300_ssd_iter_140000.caffemodel'
)

cap = cv.VideoCapture(0)

while cap.isOpened():
    r, frame = cap.read()
    if r:
        frame = cv.resize(frame, (500, 500))
        (h, w) = frame.shape[:2]
        
        blob = cv.dnn.blobFromImage(cv.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()
        
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                cv.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
        
        cv.imshow("Ram", frame)
        
        if cv.waitKey(25) & 0xFF == ord('p'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
