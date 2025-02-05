# radio button = similar to checkbox, but you can only select one from a group 
from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print('you ordered pizza')
    elif x.get() == 1:
        print('you ordered hamburger')
    elif x.get() == 2:
        print('you ordered hotdog')
    else:
        print('huh?')


window = Tk()

pizza_image = PhotoImage(file='images/pizza.png')
burger_image = PhotoImage(file='images/burger.png')
hotdog_image = PhotoImage(file='images/hotdog.png')

food_images = [pizza_image, burger_image, hotdog_image]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[index], # adds text to radio buttons
        variable=x, # groups rediobuttons together if they sharethe same variable
        value=index, # assigns each radiobutton a different value
        padx=25, # adds padding on x-axis
        font=('Impact', 50),
        image=food_images[index],# adds image to radiobutton
        compound='left', # adds image & text (left-side)
        indicatoron=0, # eliminate circle indicators
        width=600, # sets width of radio buttons
        command=order, #set command of radiobutton to function
    )
    radiobutton.pack(anchor=W)

window.mainloop()