# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(
    window,
    bg='pink',
    bd=5,
    relief=RAISED,
)
# frame.pack(side=BOTTOM)
frame.place(x=0, y=0)

# run following commented code instead of uncommented code to see what happend
# Button(window, text='W', font=('Consolas', 25), width=3).pack(side=TOP) # width is according to font size
# Button(window, text='A', font=('Consolas', 25), width=3).pack(side=LEFT) # width is according to font size
# Button(window, text='S', font=('Consolas', 25), width=3).pack(side=LEFT) # width is according to font size
# Button(window, text='D', font=('Consolas', 25), width=3).pack(side=LEFT) # width is according to font size

Button(frame, text='W', font=('Consolas', 25), width=3).pack(side=TOP) # width is according to font size
Button(frame, text='A', font=('Consolas', 25), width=3).pack(side=LEFT) # width is according to font size
Button(frame, text='S', font=('Consolas', 25), width=3).pack(side=LEFT) # width is according to font size
Button(frame, text='D', font=('Consolas', 25), width=3).pack(side=LEFT) # width is according to font size

window.mainloop()