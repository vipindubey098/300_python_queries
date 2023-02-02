from tkinter import *

#Now from the counter there is a method you can create to show window, basic window or the multi-key window
root = Tk() #This is use to create a window

root.geometry("600x250") #We set a geometry, by giving height x width


def get_value(): #This function should run whenever anyone will click on button
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    if num1 > num2:
        #Below will print on terminal:
        # print("Num1 is greater than num2")
        #To display message in window:
        Label(root, text="Num1 is greater than num2").pack()
    elif num2 > num1:
        # print("Num2 is greater than num1")
        Label(root, text="Num2 is greater than num1").pack()
    else:
        # print("Both numbers are equal")
        Label(root, text="Both numbers are equal").pack()

entry1 = Entry(root, width="40")#Entry widget to get anything from user e.g.: Input type="text", width here defines width of input type

# The Pack geometry manager packs widgets relative to the earlier widget. Tkinter literally packs all the widgets one after the other in a window.
# pack() also has padding options:
# padx, which pads externally along the x axis.
# pady, which pads externally along the y axis.
# ipadx, which pads internally along the x axis.
# ipady, which pads internally along the y axis.

# pack() positions four buttons to the left, right, top, bottom sides of a frame.
# eg: button1.pack(side = LEFT), button1.pack(side = TOP), button1.pack(side = RIGHT), button1.pack(side = BOTTOM) 

entry1.pack(pady=10) #padding via y on 10  

entry2 = Entry(root, width="40")#Entry widget to get anything from user e.g.: Input type="text", width here defines width of input type
entry2.pack()

btn = Button(root, text="Enter", command=get_value) #Button. Command is use to call function so when press it calls function and execute file
btn.pack(pady=10)

#This loop is when, user interrupt in the console or terminate a window it will stop
root.mainloop() #Root method is on main loop