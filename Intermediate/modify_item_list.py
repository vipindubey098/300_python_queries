lst = ["red","green","blue","purple"]
print(lst)
index = int(input("Enter position of item, you wanna change: "))
new_value = input("New value: ")
# subtracting -1 , because array starts with 0
lst[index-1] = new_value

print(lst)