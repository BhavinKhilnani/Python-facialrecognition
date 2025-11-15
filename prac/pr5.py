import datetime
import csv
def authenticate(gmail,password):
    # students = [s1,s2,s3,s4,s5]
    students=[]

    for student in students:
        if(student.gmail == gmail and student.password == password):
            # signin(student)
            pass

# def signin(student=object):
# signin()



def mark_attendance(student,boolean):
    writer = csv.writer()
    date_today = datetime.datetime.now().date()
    time_now = datetime.datetime.now().time()
    data = [student.name,student.rollno,time_now,boolean]
    with open(file=f"attendence_sheet_{date_today}.csv",mode="a",newline="") as File1:
        writer = csv.writer(File1)
        writer.writerow(data)

def add_rec():
    name = input("enter student's name:")
    rollno = int(input("enter student's rollno:"))
    standard = int(input("enter student's standard:"))
    section = input("enter student's section:")
    remarks = input("enter student's remarks:")
    address = input("enter student's address:")
    sub_marks = {}
    running =  True
    subjectno = 1
    while(running):
        subject = input(f"enter subject number {subjectno}:")
        marks = int(input(f"enter marks of subject number {subjectno}:"))
        subjectno+=1
        data = {subject:marks}
        sub_marks.update(data)
        ask1 = input("do you want to enter more subjects (y/n):")
        if(ask1=="y"):
            pass
        elif(ask1=="n"):
            running = False
        else:
            print("invalid input...")
            running = False
    
    # s6 = student(name,rollno,standard,section,sub_marks,remarks,address)
    
    # subject_marks = s6.sub_marks.values()

    # print(subject_marks)
    # print(s6.get_data())

add_rec()