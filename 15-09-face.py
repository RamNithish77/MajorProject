import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image = cv2.imread(r'E:\opencv\images.jpeg')
image = cv2.resize(image,(500,500))
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=1, minSize=(100, 100))
print(len(faces))
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0,255, 0), thickness=3)
cv2.imshow('Face Detection', image)
cv2.waitKey(0) 
cv2.destroyAllWindows()