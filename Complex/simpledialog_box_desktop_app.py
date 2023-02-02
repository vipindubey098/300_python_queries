from tkinter import *
from tkinter import simpledialog

root = Tk()

number = simpledialog.askinteger("Input", "Enter a number", parent=root)
print(number*number)
root.mainloop()
