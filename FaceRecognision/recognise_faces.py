import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_face_data.yml')

label_map = np.load('label_map.npy', allow_pickle=True).item()

CONFIDENCE_THRESHOLD = 50
MAX_CONFIDENCE = 255.0

cap = cv2.VideoCapture(0)

flip_vertical = False
flip_horizontal = False
rotate = False
grayscale = False
hsv = False
lab = False
blur = False
median_filter = False
draw_shapes = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    for (x, y, w, h) in faces:
        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face, (200, 200))

        label_id, confidence = recognizer.predict(face)

        if confidence < CONFIDENCE_THRESHOLD:
            person_name = label_map.get(label_id, "Unknown")
            display_text = f"{person_name} - Confidence: {100 - (confidence / MAX_CONFIDENCE * 100):.2f}%"
            color = (255, 0, 0)
        else:
            display_text = "Unknown"
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(
            frame,
            display_text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            1
        )

    if flip_vertical:
        frame = cv2.flip(frame, 0)
    if flip_horizontal:
        frame = cv2.flip(frame, 1)
    if rotate:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    if grayscale:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif hsv:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    elif lab:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    if blur:
        frame = cv2.GaussianBlur(frame, (15, 15), 0)
    if median_filter:
        frame = cv2.medianBlur(frame, 5)
    if draw_shapes:
        cv2.rectangle(frame, (50, 50), (150, 150), (0, 255, 0), 3)
        cv2.circle(frame, (200, 200), 50, (255, 0, 0), 3)

    cv2.imshow('Face Recognition with Effects', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('v'):
        flip_vertical = not flip_vertical
    elif key == ord('h'):
        flip_horizontal = not flip_horizontal
    elif key == ord('r'):
        rotate = not rotate
    elif key == ord('g'):
        grayscale = not grayscale
        hsv, lab = False, False
    elif key == ord('s'):
        hsv = not hsv
        grayscale, lab = False, False
    elif key == ord('l'):
        lab = not lab
        grayscale, hsv = False, False
    elif key == ord('b'):
        blur = not blur
    elif key == ord('n'):
        median_filter = not median_filter
    elif key == ord('d'):
        draw_shapes = not draw_shapes
    elif key == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

