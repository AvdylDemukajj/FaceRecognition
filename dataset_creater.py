import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def insertOrUpdate(Id, Name, Age):
    conn = sqlite3.connect('FaceBase.db')
    query = "SELECT * FROM Students WHERE Id ="+str(Id)
    cursor = conn.execute(query)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist==1):
        conn.execute("Update Students SET Name=? WHERE Id=?",(Name, Id))
        conn.execute("Update Students SET Age=? WHERE Id=?",(Age, Id))
    else:
        conn.execute("INSERT INTO Students (Id, Name, Age) VALUES(?,?,?)",(Id, Name, Age))

    conn.commit()
    conn.close()