import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

def insertOrUpdate(Name, Age):
    conn = sqlite3.connect('sqlite.db')
    cursor = conn.execute("SELECT Id FROM Students WHERE Name=? AND Age=?", (Name, Age))
    data = cursor.fetchone()

    if data:
        Id = data[0]
    else:
        conn.execute("INSERT INTO Students (Name, Age) VALUES(?,?)", (Name, Age))
        Id = cursor.lastrowid

    conn.commit()
    conn.close()
    return Id

Name = input('Enter User Name: ')
Age = input('Enter User Age: ')

Id = insertOrUpdate(Name, Age)

sampleNum = 0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        sampleNum += 1
        cv2.imwrite(f"dataSet/User.{Id}.{sampleNum}.jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.waitKey(100)
    cv2.imshow('Face', img)
    cv2.waitKey(1)
    if sampleNum > 20:
        break

cam.release()
cv2.destroyAllWindows()
