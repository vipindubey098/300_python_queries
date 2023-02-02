user_set = {"abc", "xyz", "pqr", "stu"}
print(user_set)
r = input("Enter a item to removal: ")
user_set.remove(r)
print(user_set)
print("Removed str: "+str(r))
user_set.add(r)
print(user_set)