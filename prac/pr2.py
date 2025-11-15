import math

class student():
    age = 0
    Name = ""
    standard = 0
    section = ""
    sub_marks = {}
    remarks = ""

ansh = student()
ansh.age = 17
ansh.standard = 12
ansh.section = "c"
ansh.Name = "ansh"
ansh.sub_marks = {"maths":51,"physics":45,"chemistry":64}



# print(get_grade(get_tot(ansh.sub_marks)))

def show_details(stud):
    
    def get_tot(sub_marks):
        total = 0
        sub_count = 0
        for key in sub_marks:
            sub_count+=1
            total = total + sub_marks[key]
        avg = total // sub_count
        print("total:",total)
        return [total,sub_count]


    def get_grade(arg1):
        total = arg1[0]
        sub_count = arg1[1]
        max_marks=sub_count*100
        '''
        100-90 A grade
        89-80 B grade
        79-50 C grade
        49-35 D grade
        34- 0 E grade (fail)
        '''
        percentage =   total * 100 // max_marks  
        print("percentage:",percentage)
        if (percentage <= 100 and percentage >=90 ):
            return "A grade"
        elif(percentage <= 89 and percentage >=80  ):
            return "B grade"
        elif(percentage <= 79 and percentage >= 50  ):
            return "C grade"
        elif(percentage <= 49 and percentage >= 35  ):
            return "D grade"
        elif(percentage <= 34 and percentage >= 0  ):
            return "E grade(failed)"
        else:
            return False
        
    
    print("--------------------------------------------------------")
    print("NAME:",stud.Name)
    print("AGE:",stud.age)
    print("STANDARD:",stud.standard)
    print("SECTION:",stud.section)
    print("\nSubject Wise Marks\n")
    for key in stud.sub_marks:
        print("       ",key,":",stud.sub_marks[key])
    print("\n")
    print("REMARKS:",stud.remarks)
    print(get_grade(get_tot(stud.sub_marks)))
    print("--------------------------------------------------------")

show_details(ansh)