# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print('Hello ' + username)

def delete():
    entry.delete(0, END) # deletes the line of text

def backspace():
    entry.delete(len(entry.get()) - 1, END)

window = Tk()


submit_btn = Button(
    window,
    text='submit',
    command=submit
)
submit_btn.pack(side = RIGHT)

delete_btn = Button(
    window,
    text='delete',
    command=delete
)
delete_btn.pack(side = RIGHT)

backspace_btn = Button(
    window,
    text='backspace',
    command=backspace
)
backspace_btn.pack(side = RIGHT)

entry = Entry()

entry.config(font=('Ink Free', 50))

entry.config(bg='black')

entry.config(fg='#00ff00')

# entry.insert(0, 'Spangebob')

# entry.config(state=DISABLED) 

entry.config(width=10)

# entry.config(show='*') # this can use for password

entry.pack()



window.mainloop()