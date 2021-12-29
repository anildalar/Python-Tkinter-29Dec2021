#Import the Tkinter Library
from tkinter import *

#Create an instance of Tkinter Frame
win = Tk()
 
# Setting the title and geometry of the app
win.title('OKLABS App')
#win.attributes('-fullscreen', True)
win.state("zoomed")
#win.geometry('600x400')
 
menubar = Menu()
     
# Declare file and edit for showing in menu bar
file = Menu(menubar, tearoff = False)
edit = Menu(menubar, tearoff = False)

# Display file and edit declared in previous step
menubar.add_cascade(label = 'File', menu = file)
menubar.add_cascade(label = 'Edit', menu = edit)

# Display of menu bar in the app
win.config(menu = menubar)

def quit_program(event):
    win.destroy()

#Bind the Keyboard shortcut Key
win.bind('<Control-x>', quit_program)

win.mainloop()