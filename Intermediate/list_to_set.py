item_list = []
for i in range(5):
    item = input("Enter "+str(i+1)+" Elements: ")
    item_list.append(item)
print("List elements are: "+str(item_list))
item_set = set(item_list)

print("Set elements are: "+str(item_set))