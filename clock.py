#My First Clock in Python - GD

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('My Clock')
root.iconbitmap(r'C:\Users\gauravsinh.dodiya\OneDrive - Reliance Corporate IT Park Limited\Desktop\My Clock\clock.ico')

def time():
	string = strftime('%H:%M:%S %p %d-%m-%y')
	lbl.config(text = string)
	lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 40, 'bold'),
			background = 'black',
			foreground = 'white')

lbl.pack(anchor = 'center')
time()

mainloop()




