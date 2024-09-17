import cv2 as cv
import numpy as np
import tensorflow as tf


model = tf.keras.models.load_model('face_detection_model.h5')

import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)
cap = cv.VideoCapture(0)

def preprocess_image(image):
    """Preprocess image for TensorFlow model."""
    image = cv.resize(image, (150, 150))  
    image = cv.cvtColor(image, cv.COLOR_GRAY2RGB)  
    image = image / 255.0
    return np.expand_dims(image, axis=0)

while cap.isOpened():
    r, frame = cap.read()
    if r:
       
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        rgb_frame = cv.cvtColor(gray_frame, cv.COLOR_GRAY2RGB)
        
    
        results = face_detection.process(rgb_frame)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw = gray_frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                
               
                cv.rectangle(gray_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                
                face_region = gray_frame[y:y+h, x:x+w]
                if face_region.size > 0:

                    face_image = preprocess_image(face_region)
                    
                   
                    prediction = model.predict(face_image)
                    print("Prediction:", prediction)

        
        cv.imshow("Face Detection", gray_frame)

        if cv.waitKey(25) & 0xFF == ord('p'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
