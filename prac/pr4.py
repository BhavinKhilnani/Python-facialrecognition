import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv #type: ignore
import datetime
import csv

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def authenticate(gmail,password):
    #will fetch data from a database and a server
    #gmail being the mail id which was requested to the server
    #student being the list of existing student entries 

    students=[]
    for student in students:
        if(student.gmail == gmail and student.password == password):
            # signin(student)
            # will show the user dashboard

            pass
def mark_attendance(student,boolean):
    writer = csv.writer()
    date_today = datetime.datetime.now().date()
    time_now = datetime.datetime.now().time()
    data = [student.name,student.rollno,time_now,boolean]
    with open(file=f"attendence_sheet_{date_today}.csv",mode="a",newline="") as File1:
        writer = csv.writer(File1)
        writer.writerow(data)
def send_email(recepient_email,mail_subject,body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recepient_email
        msg['Subject'] = mail_subject

        msg.attach(MIMEText(body,'plain'))
        with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS,recepient_email,msg.as_string())
        print("email has been sent sucessfully !!")
    except Exception as e:
        print(e)
        print("failed to send the mail :( .")
def limit(lst):
    return lst[0]

class student():
    def __init__(self,name,rollno,standard,section,sub_marks,remarks,address,password,gmail):
        self.name = name
        self.rollno = rollno
        self.standard = standard
        self.section = section
        self.address = address
        self.sub_marks = sub_marks
        self.remarks = remarks
        self.password = password
        self.gmail = gmail
    def get_data(self):
        total = 0
        sub_marks = self.sub_marks
        for i in list(sub_marks):
            total = total+sub_marks[i]
        self.total = total
        self.avg = self.total//len(self.sub_marks)
        self.percentage =  self.total  // len(self.sub_marks) 
        if (self.percentage <= 100 and self.percentage >=90 ):
            self.grade = "A grade"
        elif(self.percentage <= 89 and self.percentage >=80 ):
            self.grade = "B grade"
        elif(self.percentage <= 79 and self.percentage >= 50 ):
            self.grade = "C grade"
        elif(self.percentage <= 49 and self.percentage >= 35 ):
            self.grade = "D grade"
        elif(self.percentage <= 34 and self.percentage >= 0 ):
            self.grade = "E grade(failed)"
        else:
            self.grade = False
        highest_marks = {"none":0}
        highest_sub = "none"
        print(f"--------------------------------------------------------\nName :   {self.name} \nRoll No. : {self.rollno}\nStandard : {self.standard} \nSection :   {self.section} \nAddress :  {self.address} \nSubject Wise Marks\n")
        for key in self.sub_marks:
            if (self.sub_marks[key] > list(highest_marks.values())[0]):
                highest_sub = key
                highest_marks.clear()
                highest_marks = { key : self.sub_marks[key] }
            elif(self.sub_marks[key] == list(highest_marks.values())[0] ):
                highest_marks = { key : self.sub_marks[key] }
            print("       ",key,":",self.sub_marks[key])
        if(len(highest_marks)>1):
            print(f"{self.name} has obtained the highest marks in the subjects {highest_marks.keys()} : {limit(highest_marks.values())}")
        elif(len(highest_marks)==1):
            print(f"{self.name} has obtained the highest marks in the subject {list(highest_marks.keys())[0]} : {list(highest_marks.values())[0]}")
        print(f"Remarks :  {self.remarks} \nTotal Marks : {self.total} \n Percentage : {self.percentage}%\n--------------------------------------------------------")
        recepient = self.gmail
        mail_subject = f"Student Progress Reports – {self.standard}{self.section}" 
        body = f"""
Dear {self.name},

Here is your progress report for Standard {self.standard}, Section {self.section}:

Roll Number: {self.rollno}
Address: {self.address}

Subject-wise Marks:
""" + "\n".join([f"{sub}: {mark}" for sub, mark in self.sub_marks.items()]) + f"""

Total Marks: {self.total}
Percentage: {self.percentage}%
Grade: {self.grade}
Remarks: {self.remarks}

Highest Scoring Subject: {list(highest_marks.keys())[0]} ({list(highest_marks.values())[0]} marks)

Keep up the good work!

Regards,  
Bhavin
"""
        send_email(recepient_email=recepient,mail_subject=mail_subject,body=body)

















































































































































# if __name__ == "__main__":
#     recepient = "bhavinkhilnani@gmail.com"
#     subject = "Test Email – Please Ignore" 
#     body = "Hello,\n\n\tThis is a test email sent for\n\temonstration purposes only.\n\tPlease disregard this message.\n\nBest regards,\nBhavin"
#     # send_email(recepient_email=recepient,subject=subject,body=body)

# s1 = student("Aryan Patel", 101, 10, "A",
#              {"Math": 95, "Science": 93, "English": 90, "Social": 88, "Hindi": 92},
#              "Excellent", "21, Shiv Nagar, Surat")

# s2 = student("Meera Shah", 102, 10, "A",
#              {"Math": 60, "Science": 58, "English": 65, "Social": 70, "Hindi": 55},
#              "Needs improvement", "45, Green Park, Ahmedabad")

# s3 = student("Rahul Mehta", 103, 10, "A",
#              {"Math": 85, "Science": 82, "English": 87, "Social": 80, "Hindi": 84},
#              "Very good", "12, Laxmi Society, Rajkot")

# s4 = student("Priya Desai", 104, 10, "A",
#              {"Math": 78, "Science": 80, "English": 75, "Social": 72, "Hindi": 76},
#              "Good", "33, Shanti Nagar, Vadodara")

# s5 = student("Karan Trivedi", 105, 10, "A",
#              {"Math": 98, "Science": 98, "English": 98, "Social": 95, "Hindi": 97},
#              "Outstanding", "9, Neelkanth Colony, Bhavnagar")
# print(s1.get_data())
# print(s2.get_data())
# print(s3.get_data())
# print(s4.get_data())
# print(s5.get_data())

# records = [s1,s2,s3,s4,s5]




# def add_rec():
#     name = input("enter student's name:")
#     rollno = int(input("enter student's rollno:"))
#     standard = int(input("enter student's standard:"))
#     section = input("enter student's section:")
#     remarks = input("enter student's remarks:")
#     address = input("enter student's address:")
#     sub_marks = {}
#     running =  True
#     subjectno = 1
#     while(running):
#         subject = input(f"enter subject number {subjectno}:")
#         marks = int(input(f"enter marks of subject number {subjectno}:"))
#         subjectno+=1
#         data = {subject:marks}
#         sub_marks.update(data)
#         ask1 = input("do you want to enter more subjects (y/n):")
#         if(ask1=="y"):
#             pass
#         elif(ask1=="n"):
#             running = False
#         else:
#             print("invalid input...")
#             running = False
    
#     s6 = student(name,rollno,standard,section,sub_marks,remarks,address)
    
#     subject_marks = s6.sub_marks.values()

#     print(subject_marks)
#     print(s6.get_data())

# add_rec()

