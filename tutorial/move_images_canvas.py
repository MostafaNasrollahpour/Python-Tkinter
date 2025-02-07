from tkinter import *

def move_up(event: Event):
    canvas.move(canvas_image, 0, -10)

def move_down(event: Event):
    canvas.move(canvas_image, 0, 10)

def move_left(event: Event):
    canvas.move(canvas_image, -10, 0)

def move_right(event: Event):
    canvas.move(canvas_image, 10, 0)

window = Tk()

window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

my_image = PhotoImage(file='images/car.png')

canvas_image = canvas.create_image(0, 0, image=my_image, anchor=NW)

window.mainloop()