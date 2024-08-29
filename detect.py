import cv2
import numpy as np
import os
import sqlite3

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/training.yml")

def getprofile(id):
    conn = sqlite3.connect("sqlite.db")
    cursor = conn.execute("SELECT * FROM users WHERE Id=?", (id,))
    profile = None

    for row in cursor:
        profile = row
    conn.close()
    return profile