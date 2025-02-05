from tkinter import *

def display():
    if x.get() == 1 and y.get() == 1:
        print('I like both')
    elif x.get() == 1 and y.get() == 0:
        print("I like Python")
    elif x.get() == 0 and y.get() == 1:
        print("I like Java")
    else:
        print("I don't like either")

window = Tk()

x = IntVar()
y = IntVar()

checkbox = Checkbutton(
    window,
    text='Python',
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display
)
checkbox.config(font=('Arial', 20))
checkbox.config(fg='#0000ff')
checkbox.config(bg='#000000')
checkbox.config(activebackground='#0000ff')
checkbox.config(activeforeground='#000000')
photo = PhotoImage(file='images/python.png')
checkbox.config(image=photo) # set image to photimage 
checkbox.config(compound='left')
checkbox.config(padx=25, pady=10)
checkbox.config(width=300, height=250)
checkbox.config(anchor='w') # anchors widget to relative cardineldirection
checkbox.pack()

checkbox2 = Checkbutton(
    window,
    text='Java',
    variable=y,
    onvalue=1,
    offvalue=0,
    command=display
)
checkbox2.config(font=('Arial', 20))
checkbox2.config(fg='#0000ff')
checkbox2.config(bg='#000000')
checkbox2.config(activebackground='#0000ff')
checkbox2.config(activeforeground='#000000')
photo2 = PhotoImage(file='images/java.png')
checkbox2.config(image=photo2) # set image to photimage 
checkbox2.config(compound='left')
checkbox2.config(padx=25, pady=10)
checkbox2.config(width=300, height=250)
checkbox2.config(anchor='w') # anchors widget to relative cardineldirection
checkbox2.pack()

window.mainloop()