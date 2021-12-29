
from tkinter import *

# 1. Create the Main window

win = Tk() # Tk is a class of Tkinter
win.title('Visual Studio Code')
win.state('zoomed')
try:
  win.iconbitmap('app.ico')
except:
  print("")



menubar = Menu() # Menu is a Class of Tkinter Library
file = Menu(menubar, tearoff = False)
edit = Menu(menubar, tearoff = False)
selection = Menu(menubar, tearoff = False)
view = Menu(menubar, tearoff = False)
go = Menu(menubar, tearoff = False)
run = Menu(menubar, tearoff = False)
terminal = Menu(menubar, tearoff = False)
help = Menu(menubar, tearoff = False)

menubar.add_cascade(label='File',menu =file)
menubar.add_cascade(label='Edit',menu =edit)
menubar.add_cascade(label='Selection',menu =selection)
menubar.add_cascade(label='View',menu =view)
menubar.add_cascade(label='Go',menu =go)
menubar.add_cascade(label='Run',menu =run)
menubar.add_cascade(label='Terminal',menu =terminal)
menubar.add_cascade(label='Help',menu =help)

win.config(menu = menubar)

#2. Run the mainloop


win.mainloop()