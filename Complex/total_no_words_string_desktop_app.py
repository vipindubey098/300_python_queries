from tkinter import *
root = Tk()
root.geometry("600x250")
def get_value():
    user_string = entry.get()
    total_char = len(user_string)
    sp = 0
    for i in user_string:
        if i.isspace():
            sp += 1
    total_words = sp+1
    Label(root, text="Total char: "+str(total_char)).pack()
    Label(root, text="Total words: "+str(total_words)).pack()
    Label(root, text="Total space: "+str(sp)).pack()
entry = Entry(root, width="40")
entry.pack(pady=10) 
btn = Button(root, text="Enter", command=get_value) 
btn.pack(pady=10)
root.mainloop()