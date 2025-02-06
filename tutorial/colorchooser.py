from tkinter import *
from tkinter import colorchooser # submodule

def click():
    color = colorchooser.askcolor()
    # print(color) # print it for study goals
    color_hex = color[1]
    window.config(bg=color_hex) # change background color

window = Tk()

window.geometry('420x420')

button = Button(text='click me', command=click)
button.pack()

window.mainloop()