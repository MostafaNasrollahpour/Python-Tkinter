# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    input = text.get('1.0', END)
    print(input)

window = Tk()

text = Text(
    window, 
    bg='light yellow',
    font=("Ink Free", 25), # width and height of window change according to font size
    height=8,
    width=20,
    padx=20,
    pady=20,
    fg='purple'
)

text.pack()

button = Button(window, command=submit, text='submint')
button.pack()

window.mainloop()