import random
from tkinter import *

root = Tk()
people = list(range(1, 34))
random.shuffle(people)
people.append(0)
people.append(0)
people.append(0)

at = 0

for i in range(6):
    for j in range(3):
        label1 = str(people[at])
        label2 = str(people[at + 1])
        if len(label1) == 1:
            label1 = "0" + label1
        if len(label2) == 1:
            label2 = "0" + label2
        button1 = Button(root, text=label1, height=2, width=6)
        button2 = Button(root, text=label2, height=2, width=6)
        at += 2

        button1.grid(row=i, column=2 * j, padx=(10,0))  
        button2.grid(row=i, column=2 * j + 1,)
        

root.mainloop()
