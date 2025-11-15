from tkinter import *
from save import save_history, view_history
strr = ""
def press(char):
    global strr
    strr = strr + str(char)
    result.set(strr)
def submit():
    try:
        global strr
        try:
            save_history(strr)
        except:
            print("Error ")

        total = str(eval(strr))

        result.set(total)

        strr = total
    except:

        result.set(" error ")
        strr = ""
def clear():
    global strr
    strr = ""
    result.set("")
def remove1():
    global strr
    strr = strr[:-1]
    result.set(strr)
# Driver code
root = Tk()
root.configure(background="white")
root.title("Simple Calculator")
root.geometry("335x570")
root.maxsize(width=335, height=570)
root.minsize(width=335, height=570)
result = StringVar()
strr_field = Entry(root, textvariable=result,width=30,font=("Arial", 30) ,state="disabled")
    #height of the entry field is manipulated by font size
strr_field.grid(columnspan=100 )
button1 = Button(
        root,
        text=" 1 ",
        fg="white",
        bg="black",
        command=lambda: press(1),
        height=5,
        width=10,
    )
button1.grid(row=2, column=0)
button2 = Button(
        root,
        text=" 2 ",
        fg="white",
        bg="black",
        command=lambda: press(2),
        height=5,
        width=10,
    )
button2.grid(row=2, column=1)
button3 = Button(
        root,
        text=" 3 ",
        fg="white",
        bg="black",
        command=lambda: press(3),
        height=5,
        width=10,
    )
button3.grid(row=2, column=2)
button4 = Button(
        root,
        text=" 4 ",
        fg="white",
        bg="black",
        command=lambda: press(4),
        height=5,
        width=10,
    )
button4.grid(row=3, column=0)
button5 = Button(
        root,
        text=" 5 ",
        fg="white",
        bg="black",
        command=lambda: press(5),
        height=5,
        width=10,
    )
button5.grid(row=3, column=1)
button6 = Button(
        root,
        text=" 6 ",
        fg="white",
        bg="black",
        command=lambda: press(6),
        height=5,
        width=10,
    )
button6.grid(row=3, column=2)
button7 = Button(
        root,
        text=" 7 ",
        fg="white",
        bg="black",
        command=lambda: press(7),
        height=5,
        width=10,
    )
button7.grid(row=4, column=0)
button8 = Button(
        root,
        text=" 8 ",
        fg="white",
        bg="black",
        command=lambda: press(8),
        height=5,
        width=10,
    )
button8.grid(row=4, column=1)
button9 = Button(
        root,
        text=" 9 ",
        fg="white",
        bg="black",
        command=lambda: press(9),
        height=5,
        width=10,
    )
button9.grid(row=4, column=2)
button0 = Button(
        root,
        text=" 0 ",
        fg="white",
        bg="black",
        command=lambda: press(0),
        height=5,
        width=10,
    )
button0.grid(row=5, column=0)
plus = Button(
        root,
        text=" + ",
        fg="white",
        bg="black",
        command=lambda: press("+"),
        height=5,
        width=10,
    )
plus.grid(row=2, column=3)
minus = Button(
        root,
        text=" - ",
        fg="white",
        bg="black",
        command=lambda: press("-"),
        height=5,
        width=10,
    )
minus.grid(row=3, column=3)
multiply = Button(
        root,
        text=" * ",
        fg="white",
        bg="black",
        command=lambda: press("*"),
        height=5,
        width=10,
    )
multiply.grid(row=4, column=3)
divide = Button(
        root,
        text=" / ",
        fg="white",
        bg="black",
        command=lambda: press("/"),
        height=5,
        width=10,
    )
divide.grid(row=5, column=3)
equal = Button(
        root, text=" = ", fg="white", bg="black", command=submit, height=5, width=10
    )
equal.grid(row=5, column=2)
clear = Button(
        root, text="Clear", fg="white", bg="black", command=clear, height=5, width=10
    )
clear.grid(row=5, column=1)
Decimal = Button(
        root,
        text=".",
        fg="white",
        bg="black",
        command=lambda: press("."),
        height=5,
        width=10,
    )
Decimal.grid(row=6, column=0)
view_history = Button(
        root, text="View History", fg="white", bg="black", command=view_history, height=5, width=10
    )
view_history.grid(row=6, column=1)
backspace = Button(
        root,
        text="←",
        fg="white",
        bg="black",
        command=remove1,
        height=5,
        width=10,)
backspace.grid(row=6, column=2)
bracket_open = Button(
    root,
    text="(",
    fg="white",
    bg="black",
    command=lambda: press("("),
    height=5,
    width=10,
)
bracket_open.grid(row=6, column=3)
bracket_close = Button(
    root,
    text=")",
    fg="white",
    bg="black",
    command=lambda: press(")"),
    height=5,
    width=10,
)
bracket_close.grid(row=7, column=3)
root.mainloop()

# numbers= ["1","2","3","4","5","6","7","8","9","0"]
# def evaluate(str):
#     #5+7+5-2*3
#     result = 0
#     num = 0
#     operation = ""
#     for i in str:
#         if(i in numbers):
#             num = num*10 + int(i)
#         else:
#             operation = i
#             if (operation == "+"):
#                 result = result + num
#             elif(operation == "-"):
#                 result = result - num
#             elif(operation == "/"):
#                 result = result/num
#             elif(operation == "//"):
#                 result = result // num
#             elif(operation == "*"):
#                 result = result * num
#             elif(operation == "**"):
#                 result = result**num
#             elif(operation == "%"):
#                 result = result%num
#             num = 0
#     return result

# print(evaluate("5+5+7+5"))


            
            # num = 0
            # checkresult()
def checkresult():
    pass
