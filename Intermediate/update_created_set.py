st = {"pink","white","black"}
print(st)
item = input("Enter item to update a set: ")
user_item = {item}
st.update(user_item)
print(st)