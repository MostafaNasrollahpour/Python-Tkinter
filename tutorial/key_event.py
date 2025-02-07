from tkinter import *

def do_sth(event):
    # print('you pressed: ' + event.keysym)
    label.config(text=event.keysym)

window = Tk()

# form:
# window.bind(event, function)

window.bind('<Key>', do_sth) # we can use these too: Down/Up/Return/Key

label = Label(window, font=('Helvetica', 100))
label.pack()

window.mainloop()