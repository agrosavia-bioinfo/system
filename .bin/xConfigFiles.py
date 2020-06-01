#!/usr/bin/python3
import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("pdf",1),
    ("img",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def leftKey(event):
    print ("Left key pressed")

def rightKey(event):
    print ("Right key pressed")

def ShowChoice():
	print(v.get())
	option = v.get()
	if (option==0):
		print ("Python")
	

tk.Label(root, 
         text="Select config file",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.bind ("<Up>", leftKey)
root.bind ("<Down>", rightKey)
root.focus_set()



root.mainloop()
