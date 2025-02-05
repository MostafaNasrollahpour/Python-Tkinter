from tkinter import *

# button = you click it, then it does stuff

def click():
    print('Hello')

window = Tk()

button = Button(window, text='Click me!!!')

button.config(command=click)

button.config(font=('Ink Free', 50, 'bold'))

button.config(bg='#ff6200')

button.config(fg='#fffb1f')

button.config(activebackground='red')

button.config(activeforeground='#fffb1f')

image = PhotoImage(file='images/button.png')

button.config(image=image)

button.config(compound='bottom')

# button.config(state=DISABLED) #disabled button (ACTIVE/DISABLED)

button.pack()

window.mainloop()