import cv2 as cv
import mediapipe as mp
import tensorflow as tf
import numpy as np
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)
mp_drawing = mp.solutions.drawing_utils
cap = cv.VideoCapture(0)
def preprocess_image(image):
    """Preprocess image for TensorFlow model if needed."""
    image = cv.resize(image, (150, 150)) 
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    image = image / 255.0
    return np.expand_dims(image, axis=0)

while cap.isOpened():
    r, frame = cap.read()
    if r:
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                mp_drawing.draw_detection(frame, detection)
                face_region = frame[y:y+h, x:x+w]
                if face_region.size > 0:
                    face_image = preprocess_image(face_region)
                    pass
        cv.imshow("Face Detection", frame)

        if cv.waitKey(25) & 0xFF == ord('p'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
