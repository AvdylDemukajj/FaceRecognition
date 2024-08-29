import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()

path = "dataSet"


def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpg")]
    faces = []
    Ids = []

    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert("L")
        faceNp = np.array(faceImage, np.uint8)
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        print(Id)
        faces.append(faceNp)
        Ids.append(Id)
        cv2.imshow("Training", faceNp)
        cv2.waitKey(10)
    return np.array(Ids), faces

Ids, faces = getImagesWithID(path)
recognizer.train(faces, Ids)
recognizer.save("recognizer/training.yml")
cv2.destroyAllWindows()