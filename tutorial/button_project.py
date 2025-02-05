from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count += 1
    label.config(text=count)

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

# for show count
label = Label(window, text=count)
label.config(font=('Monospace', 50))
label.pack()
# end of show

button.pack()

window.mainloop()