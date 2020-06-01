#!/usr/bin/python
import commands
from Tkinter import Tk,IntVar,Scale

def adjustVol(vol):
	commands.getoutput("/usr/sbin/mixer vol "+vol)
	return

root = Tk()
root.geometry('50x100+80+620')
vol = IntVar()
scale = Scale(root,variable=vol,from_=100,to=0,command=adjustVol)
scale.set(commands.getoutput('/usr/sbin/mixer -S').split(':')[1])
scale.pack()
root.mainloop()
