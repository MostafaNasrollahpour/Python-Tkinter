from tkinter import *
from tkinter import messagebox # import messagebox library

def click():
    # messagebox.showinfo(
    #     title='this is an info message box',
    #     message='you are a person',
    # )

    # messagebox.showwarning(
    #     title='Warning!',
    #     message='you have a virus!!',
    # )

    # messagebox.showerror(
    #     title='error',
    #     message='something went wrong',
    # )

    # x = messagebox.askokcancel( # this return a true or false
    #     title='ask ok cancel',
    #     message='do you want to do the thing?',
    # )
    # if x:
    #     print('you did a thing')
    # else:
    #     print('you canceled a thing')

    # x = messagebox.askretrycancel( # this return a true or false
    #     title='ask ok cancel',
    #     message='do you want to retry the thing?',
    # )
    # if x:
    #     print('you retried a thing')
    # else:
    #     print('you canceled a thing')

    # x = messagebox.askyesno( # this return a true or false
    #     title='ask yes or no',
    #     message='do you like cake',
    # )
    # if x:
    #     print('I like cake too')
    # else:
    #     print('why do you not like cake?')

    # answer = messagebox.askquestion( # this return a string
    #     title='ask question',
    #     message='Do you like pie?'
    # )
    # if answer == 'yes':
    #     print('i like pie too')
    # else:
    #     print('why do you not like pie?')
    
    answer = messagebox.askyesnocancel(
        title='yes no cancel',
        message='do like to code?',
        icon='warning', # you can use info/error too
    )
    if answer == True:
        print('you like to code')
    elif answer == False:
        print('then why are you watching a video on coding?')
    else:
        print('you have dodged the question')

window = Tk()

button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()