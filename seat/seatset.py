import random

from tkinter import *

root = Tk()
people=list(range(1,34))
random.shuffle(people)
people.append(0)
people.append(0)
people.append(0)


at = 0

for i in range(6):
    for j in range(6):
        label = str(people[at])
        if len(label) == 1: label = "0"+label
        button = Button(root, text=label, height=5, width=10)
        at += 1

        button.grid(row=i, column=j+j,padx=10)


root.mainloop()