from tkinter import *
from tkinter import messagebox

def show_answer():
    Ans = int(num1.get()) + int(num2.get())
    messagebox.showinfo('answer',Ans)

main = Tk()
w, h = main.winfo_screenwidth(), main.winfo_screenheight()
main.geometry("%dx%d+0+0" % (w, h))

Label(main, text="Enter Num 1:").grid(row=0)
Label(main, text="Enter Num 2:").grid(row=1)

num1 = Entry(main)
num2 = Entry(main)

num1.grid(row=0,column=1)
num2.grid(row=1,column=1)

Button(main,text='Quit',command=main.destroy).grid(row=4,column=0,sticky=W,pady=4)
Button(main,text='Show',command=show_answer).grid(row=4,column=1,sticky=W,pady=4)

mainloop()