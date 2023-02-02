# lst = {} #this won't work, it won't work use below thing
lst = set()
for i in range(6):
    enter_data = input("Enter "+str(i+1)+" number: ")
    lst.add(enter_data)
print(lst)
lst.clear()
print(lst)