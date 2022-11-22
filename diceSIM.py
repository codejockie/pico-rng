from tkinter import *
import random

from Comms import Comms

# Creating a window
window = Tk()

# Configuring of the window
window.configure(bg="black")
window.geometry("550x350")
window.title("Roll The Dice")

comms = Comms()

# dice face images
diceimg = ['\u2680', '\u2681',
           '\u2682', '\u2683',
           '\u2684', '\u2685']

rolledimg = ['\u2680']  # slected number/rolled number

# Dice Roll simulation


def delay():
    # label.configure(text=f'\u2680')
    label.configure(
        text=f'{random.choice(diceimg)}')
    window.after(100, d1)


def d1():
    # label.configure(text=f'\u2681')
    label.configure(
        text=f'{random.choice(diceimg)}')
    window.after(100, d2)


def d2():
    # label.configure(text=f'\u2682')
    label.configure(
        text=f'{random.choice(diceimg)}')
    window.after(100, d3)


def d3():
    # label.configure(text=f'\u2683')
    label.configure(
        text=f'{random.choice(diceimg)}')
    window.after(100, d4)


def d4():
    # label.configure(text=f'\u2684')
    label.configure(
        text=f'{random.choice(diceimg)}')
    window.after(100, d5)


def d5():
    # label.configure(text=f'\u2685')
    label.configure(
        text=f'{random.choice(diceimg)}')
    window.after(100, roll)

# Function that takes rolled number


def roll():
    # Roll a die
    comms.send("roll()")
    rolledNum = int(comms.receive()) - 1
    label.configure(
        text=f'{diceimg[rolledNum]}')
    label.pack()


# button
roll_button = Button(window, text="Roll!",
                     width=10, height=2,
                     font=15, bg="dimgrey",
                     bd=2, command=delay)

roll_button.pack(padx=10, pady=15)

# label to position dice
label = Label(window, font=("times", 200),
              bg="black", fg="white")

window.mainloop()
