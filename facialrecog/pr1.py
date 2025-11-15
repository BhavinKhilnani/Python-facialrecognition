from tkinter import *
import cv2
import numpy as np
import face_recognition 
from datetime import datetime
import csv
cap = cv2.VideoCapture(0)

rno_1 = face_recognition.load_image_file('./std1.jpg')
rno_1_encoding = face_recognition.face_encodings(rno_1)[0]

rno_2 = face_recognition.load_image_file('./std2.jpg')
rno_2_encoding = face_recognition.face_encodings(rno_2)[0]

rno_3 = face_recognition.load_image_file('./std3.jpg')
rno_3_encoding = face_recognition.face_encodings(rno_3)[0]

rno_4 = face_recognition.load_image_file('./std4.jpg')
rno_4_encoding = face_recognition.face_encodings(rno_4)[0]

known_face_encodings = [
    rno_1_encoding,
    rno_2_encoding,
    rno_3_encoding,
    rno_4_encoding
]

known_face_names = [
    "Student 1",
    "Student 2",
    "Student 3",
    "Student 4"
]

students = []

face_locations = []

face_encodings = []

face_names = []

s = True

now = datetime.now()

dt_string = now.strftime("%Y-%m-%d")

file = open(dt_string+'  attendance.csv' , mode='a+' , newline='')
writer = csv.writer(file)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from webcam.")
        break
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index] and any(matches):
            name = known_face_names[best_match_index]
            print(best_match_index)
            if name not in students:
                students.append(name)
                now = datetime.now().strftime("%H:%M:%S")
                writer.writerow([name, now])
                print(f"Attendance marked for {name} at {now}.")

                file.flush()
                root = Tk()
                root.title("Attendance System")
                root.geometry("500x500")
                label = Label(root, text=f"Attendance marked for {name} at {now}.")
                label.pack()
                root.after(5000, root.destroy)

                root.mainloop()
        
        face_names.append(name)
    
    
    cv2.imshow('Attendance System', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
file.close()