from tkinter import *
root = Tk()
root.geometry("600x250")
def get_value():
    user_value = int(entry.get())
    for i in range(1,11):
        # print(str(user_value)+"*"+str(i)+"="+str(user_value*i))
        Label(root, text=""+str(user_value)+"*"+str(i)+"="+str(user_value*i)+"").pack()

entry = Entry(root, width="40")
entry.pack(pady=10) 
btn = Button(root, text="Enter", command=get_value) 
btn.pack(pady=10)
root.mainloop()