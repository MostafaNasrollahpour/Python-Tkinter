from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()

hot_image = PhotoImage(file='images/hot.png')
hot_label = Label(image=hot_image)
hot_label.pack()

scale = Scale(
    window, 
    from_=0, 
    to=100,
    length=400,
    orient=VERTICAL, # orientation of scale
    font=("Consolas", 20),
    tickinterval=10, # adds numeric indicators for value
    showvalue=0, # hide current value
    resolution=5, # increment of slider
    troughcolor='#69EAFF',
    fg='#FF1C00',

)
# scale.set(50)
scale.set(((scale['from'] - scale['to'] ) / 2) + scale['to']) # set current value of slider
scale.pack()

ice_image = PhotoImage(file='images/ice.png')
ice_label = Label(image=ice_image)
ice_label.pack()

button = Button(window, text='submit', command=submit)
button.pack()
window.mainloop()