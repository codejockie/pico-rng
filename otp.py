from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("1350x800")
root.title("755 Project")
root.resizable(width=False, height=False)

def signin():
    OTP=code.get()

    if OTP=="":
        messagebox.showinfo (title="Error", message="Blank not allowed")
    elif len(str(OTP))==6:
        messagebox.showinfo (title="Successful", message="You have successfully logged in")
    else:
        messagebox.showinfo (title="Error", message="Incorrect OTP")

bg = PhotoImage(file=("Bg.png"))
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

img = PhotoImage(file=("Ncatt.png"))
Label(root,image=img,).place(x=477,y=50)

frame=Frame(root,width=500,height=500, bg="#022761", padx=30, pady=30)
frame.place(x=450,y=160)

heading=Label(frame,text="Project Raspberry PI", fg="#E8E8E8",bg="#022761",font=("Montserrat Italic",22,"bold") )
heading.place(x=100,y=40)

heading=Label(frame,text="Sign In", fg="#E8E8E8",bg="#022761",font=("Montserrat Regular",18) )
heading.place(x=40,y=130)

####---------------------------------------
def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    OTP=code.get()
    if OTP=="":
        code.insert(0,"OTP")

code = Entry(frame,width=47,fg="white",border=0,bg="#022761",font=("Montserrat Regular",13) )
code.place(y=200)
code.insert(0,"OTP")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=435,height=2,bg="white").place(y=230)

########################

Button(frame,width=45,pady=7,text="Sign In",bg="white",fg="black",border=0,command=signin).place(y=270)
label=Label(frame,text="This Project was done..... ", fg="white",bg="#022761",font=("Montserrat Regular",13))
label.place(x=100,y=350)
root.mainloop()