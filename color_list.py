lst = ['red', 'blue', 'green', 'purple']
no_of_color = int(input("Enter no. of color you want to add: "))
for i in range(no_of_color):
    lst.append(input("Enter "+str(i+1)+" color: "))
# add_data = input("Enter color you want to add: ")

# lst.append(add_data)
print(lst)
print(len(lst))