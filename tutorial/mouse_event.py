from tkinter import *

def do_sth(event: Event):
    print('position: x: ' + str(event.x) + ', y: ' + str(event.y))

window = Tk()

# window.bind('<Button-1>', do_sth) # you can use these too: Button-2/Button-3
# window.bind('<ButtonRelease>', do_sth)
# window.bind('<Enter>', do_sth)
# window.bind('<Leave>', do_sth)
window.bind('<Motion>', do_sth)

window.mainloop()