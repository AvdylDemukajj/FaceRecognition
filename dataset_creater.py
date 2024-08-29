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

Id= input('Enter User Id')
Name= input('Enter User Name')
Age= input('Enter User Age')

insertOrUpdate(Id, Name, Age)

sampleNum=0

while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        sampleNum += 1
        cv2.imwrite("dataSet/User."+str(Id)+"."+str(sampleNum)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.waitKey(100)
    cv2.imshow('Face', img)
    cv2.waitKey(1)
    if(sampleNum>20):
        break
   
