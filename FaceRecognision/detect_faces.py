import cv2
import os
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def prepare_training_data(data_folder_path):
    faces = []
    labels = []
    label_map = {}
    current_label = 0

    for person_name in os.listdir(data_folder_path):
        person_folder = os.path.join(data_folder_path, person_name)
        if not os.path.isdir(person_folder):
            continue
        label_map[current_label] = person_name

        for image_name in os.listdir(person_folder):
            image_path = os.path.join(person_folder, image_name)

            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if image is None:
                continue

            faces_detected = face_cascade.detectMultiScale(
                image,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            for (x, y, w, h) in faces_detected:
                face = image[y:y + h, x:x + w]
                face = cv2.resize(face, (200, 200))
                faces.append(face)
                labels.append(current_label)
        current_label += 1

    return faces, np.array(labels), label_map

data_folder_path = "training_data"
faces, labels, label_map = prepare_training_data(data_folder_path)

#recognizer = cv2.face.FisherFaceRecognizer_create()
#recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, labels)

recognizer.save('trained_face_data.yml')
np.save('label_map.npy', label_map)
print("Training completed and model saved as 'trained_face_data.yml'")
