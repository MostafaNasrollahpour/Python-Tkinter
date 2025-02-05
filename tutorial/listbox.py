# listbox = A listing of selectable text items within it's own container

from tkinter import *

def submit():
    print('You have ordered: ')
    # print(listbox.get(listbox.curselection()))

    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entry.get())
    listbox.config(height=listbox.size())

def delete():
    # listbox.delete(listbox.curselection())
    # listbox.config(height=listbox.size())

    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(
    window,
    bg='#f7ffde',
    font=('Constantia', 35),
    width=12,
    selectmode= MULTIPLE # if we don't write this line of code,
                        # we can use previous code that is commented now
)
listbox.pack()

listbox.insert(1, 'pizza')
listbox.insert(2, 'pasta')
listbox.insert(3, 'garlic bread')
listbox.insert(4, 'soup')
listbox.insert(5, 'salad')

listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()

submit_btn = Button(
    window, 
    text='submint',
    command=submit
)
submit_btn.pack()

add_btn = Button(
    window, 
    text='add',
    command=add
)
add_btn.pack()

delete_btn = Button(
    window, 
    text='delete',
    command=delete
)
delete_btn.pack()

window.mainloop()