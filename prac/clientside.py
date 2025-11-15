import csv
import customtkinter
import datetime

special_chars = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","\\","|","'",'"',";",":","<",">",",",".","/","?"]


def sign_in():
    gmail = input("enter gmail acc of the student:")
    password = input("enter password :")
    # send req to a server
    # button : forgot password


def submit():

    # validating the inputs
    # ent1
    if ent1.get() == "":
        print(ent1.get())
        lbl2.configure(
            text="Enter a valid name !!!",
            width=300,
            bg_color="red",
            height=50,
            corner_radius=500,
        )
    elif ent1.get() != "":
        lbl2.configure(text="", width=0, height=0, bg_color="transparent")
        for i in ent1.get():
            if (i.isnumeric()):
                lbl2.configure(
                    text="Names cant have numbers in them , silly billy .",
                    width=300,
                    bg_color="red",
                    height=50,
                    corner_radius=500,
                )
            elif(i in special_chars):
                lbl2.configure(
                    text="special chars arent allowed .",
                    width=300,
                    bg_color="red",
                    height=50,
                    corner_radius=500,
                )

            else:
                pass
    # ent2
    if ent2.get().isnumeric():
        pass
    else:
        lbl2.configure(
            text="Enter a valid rno.",
            width=300,
            bg_color="red",
            height=50,
            corner_radius=500,
        )
    # ent3
    if ent3.get().isnumeric():
        pass
    elif(int(ent3.get()>12)):
        lbl2.configure(
            text="value cannot be more than 12.",
            width=300,
            bg_color="red",
            height=50,
            corner_radius=500,
        )
    else:
        lbl2.configure(
            text="Enter a valid standard.",
            width=300,
            bg_color="red",
            height=50,
            corner_radius=500,
        )
    # ent4
    pass
    # ent5
    pass
    # ent6
    if(ent6.get().endswith('@gmail.com')):
        pass
    else:
        lbl2.configure(
            text='value should end with "@gmail.com"',
            width=300,
            bg_color="red",
            height=50,
            corner_radius=500,
        )
    #ent7
    pass

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
lbl1 = customtkinter.CTkLabel(root, text="Sign Up !", font=("Helvetica", 30))
lbl1.pack(pady=40)

ent_height = 40
ent_width = 500

ent1 = customtkinter.CTkEntry(
    root,
    placeholder_text="Enter your name ",
    width=ent_width,
    height=ent_height,
)
ent2 = customtkinter.CTkEntry(
    root,
    placeholder_text="Enter your rollno  ",
    width=ent_width,
    height=ent_height,
    state="normal",
)
ent3 = customtkinter.CTkEntry(
    root,
    placeholder_text="Enter your standard  ",
    width=ent_width,
    height=ent_height,
    state="normal",
)
ent4 = customtkinter.CTkEntry(
    root,
    placeholder_text="Enter your section  ",
    width=ent_width,
    height=ent_height,
    state="normal",
)
ent5 = customtkinter.CTkEntry(
    root,
    placeholder_text="Enter your address  ",
    width=ent_width,
    height=ent_height,
    state="normal",
)
ent6 = customtkinter.CTkEntry(
    root,
    placeholder_text="Enter your gmail ",
    width=ent_width,
    height=ent_height,
    state="normal",
)
ent7 = customtkinter.CTkEntry(
    root,
    placeholder_text="Enter your password  ",
    width=ent_width,
    height=ent_height,
    state="normal",
)
ent1.pack(pady=10)
ent2.pack(pady=10)
ent3.pack(pady=10)
ent4.pack(pady=10)
ent5.pack(pady=10)
ent6.pack(pady=10)
ent7.pack(pady=10)

btn1 = customtkinter.CTkButton(
    root,
    text="Submit!",
    command=submit,
    height=100,
    width=200,
    font=("helvetica", 24),
    hover=True,
    corner_radius=30,
)
btn1.pack(pady=20)


root.geometry("1920x1080")

lbl2 = customtkinter.CTkLabel(
    root,
    text="",
    text_color="white",
    font=("Helvetica", 18),
    height=0,
    width=0,
    corner_radius=50,
)
lbl2.pack(pady=40)
# btn2 = customtkinter.CTkButton(
#     root,
#     text="Already have an account ? Sign in instead !!! ",
#     command=sign_in,
#     height=100,
#     width=200,
#     font=(
#         "helvetica",
#         24,
#     ),
#     corner_radius=30,
#     bg_color="transparent",
#     fg_color="transparent",
#     hover=False,
#     text_color="lightblue",
# )
# btn2.pack(pady=10)
root.mainloop()


def mark_attendance(student, boolean):
    writer = csv.writer()
    date_today = datetime.datetime.now().date()
    time_now = datetime.datetime.now().time()
    data = [student.name, student.rollno, time_now, boolean]
    with open(file=f"attendence_sheet_{date_today}.csv", mode="a", newline="") as File1:
        writer = csv.writer(File1)
        writer.writerow(data)


def sign_up():
    name = input("enter student's name:")
    rollno = int(input("enter student's rollno:"))
    standard = int(input("enter student's standard:"))
    section = input("enter student's section:")
    address = input("enter student's address:")
    gmail = input("enter gmail acc of the student:")
    password = input("enter password :")
    # will send data to the server
    # then will  redirect the client to sign_in page


# sign_up()
def forgot_password(email):
    pass
    # will check if the acc already exists , if it does exist beforehand then it will send the password to the respective mail acc
    # however if it doesnt exist then it will ask the user to either check the mail id or signup
