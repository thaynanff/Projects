from tkinter import *
import random

# widget that represents tha main application
app = Tk()
app.geometry('300x400')
app.title('Dice Roller')

# label to display dice
label = Label(app, text='', font=('Helvetica', 260))

# label to display the information of what number was chosen
txt1 = Label(app, text='The number was:', font=('Helvetica', 12))

# function activated by button
def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] # unicode character strings for dice
    label.configure(text=f'{random.choice(dice)}')
    label.pack()
    txt1.place(x=85, y=80)

# button that makes the action of rolling the dice
button = Button(app, text='Roll Dice', foreground='black', command=roll_dice)

# pack a widget in the parent widget
button.pack()

# call the mainloop of Tk and keeps the window opened
app.mainloop()
