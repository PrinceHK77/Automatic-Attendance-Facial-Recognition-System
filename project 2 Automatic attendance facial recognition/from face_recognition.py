import face_recognition
import cv2
import numpy as np
import os  #To import the things present in the local system
from datetime import datetime
import csv

cap=cv2.VideoCapture(0) #To acess web-cam

hrithick_image = face_recognition.load_image_file("photos/hrithick.jpg")   #photos-location and jpg name
hrithick_encoding = face_recognition.face_encodings(hrithick_image)[0]

chethan_image = face_recognition.load_image_file("photos/chethan.jpg")
chethan_encoding = face_recognition.face_encodings(chethan_image)[0]

yashwanth_image = face_recognition.load_image_file("photos/yashwanth.jpg")
yashwanth_encoding = face_recognition.face_encodings(yashwanth_image)[0]

karthick_image = face_recognition.load_image_file("photos/karthick.jpg")
karthick_encoding = face_recognition.face_encodings(karthick_image)[0]

esakki_image = face_recognition.load_image_file("photos/esakki.jpg")
esakki_encoding = face_recognition.face_encodings(esakki_image)[0]

known_face_encoding = [
hrithick_encoding,
chethan_encoding,
yashwanth_encoding,
karthick_encoding,
esakki_encoding
]

known_face_names = [
"Hrithick Kumar - 202204016",
"Chethan - 202204016",
"Yashwanth Naidu - 202204050",
"Karthick Balaji - 202204023",
"Esakki Muthu - 202204013"
]

students = known_face_names.copy() #copid known_faces_name to list students

face_encodings= []
face_location= []  #To assign FACE CO-ORDINATES
face_names= []
s=True

now = datetime.now()
current_date = now.strftime("%y-%m-%d") #created a variable current_date

f = open(current_date+'.csv','w+',newline ='') #current_date used here to create a csv
lnwriter =csv.writer(f) #lnwriter is used to write data in csv
cap=cv2.VideoCapture(0)

while True:
    res,frame = cap.read() #this is to take input from web cam
    #print(res)
    small_frame =frame
    rgb_small_frame = small_frame[:,:,::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodin = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names =[]
    
    for face_encoding in face_encodin: #if stored face(face_encoding) matched in input(face_encodings)
        matchs = face_recognition.compare_faces(known_face_encoding,face_encoding) #comparing known_face_encoding,face_encoding
        name=""
        face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
        best_match_index = np.argmin(face_distance) # numpy argmin-To check Array of indices into the array with same shape as array
        if matchs[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
        if name in known_face_names:
            if name in students:
                students.remove(name)
                print(name,'is recognized')
                print(students)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow([name,current_time])
    cv2.imshow("attendence system",frame)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
f.close()