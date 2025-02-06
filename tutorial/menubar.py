from tkinter import *

def open_file():
    print('file has been opened!')

def save_file():
    print('file has been saved!')

def cut():
    print('you cut some text')

def copy():
    print('you copy some text')

def paste():
    print('you paste some text')

window = Tk()

open_image = PhotoImage(file='images/open-icon.png')
save_image = PhotoImage(file='images/save-icon.png')
exit_image = PhotoImage(file='images/exit-icon.png')

menubar = Menu(window)

window.config(menu=menubar)

file_menu = Menu(
    menubar,
    tearoff=0, # do not use this for see what happend
    font=('MV Boli',15),
)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label='open', command=open_file, image=open_image, compound='left')
file_menu.add_command(label='save', command=save_file, image=save_image, compound='left')
file_menu.add_separator()
file_menu.add_command(label='exit', command=quit, image=exit_image, compound='left')

edit_menu = Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label='edit', menu=edit_menu)
edit_menu.add_command(label='cut', command=cut)
edit_menu.add_command(label='copy', command=copy)
edit_menu.add_command(label='paste', command=paste)

window.mainloop()