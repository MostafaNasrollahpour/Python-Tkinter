from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='images/image.png')

label = Label(
    window, # set master of this label
    text='Hello World!',
    font=('Arial', 40, 'bold'),
    fg='#00ff00',
    bg='white',
    relief=RAISED, #SUNKEN
    bd=10,
    padx=20,
    pady=20, 
    image=photo,
    compound='bottom' # we can set photo top, left, right of our text
)

label.pack() 

# we can use place method instead of pack
# label.place(x=100, y=100)



window.mainloop()