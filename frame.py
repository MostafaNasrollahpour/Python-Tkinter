from tkinter import *

# widgets = gui elements: buttons, textboxes, labels, images
# windos = seves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window

window.geometry("430x800")

window.title("first gui programm")

icon = PhotoImage(file='images/logo.png')
window.iconphoto(True, icon)

window.config(
    background='black' #we can set hex-value to: like: '#5cfcff'
)

window.mainloop() # place window on computer screen, listen for events