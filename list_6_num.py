lst = []
# to get the number from user and store in the list
for i in range(6):
    lst.append(int(input("Enter "+str(i+1)+" no.: ")))
print(lst)

# Sum the number of list
s = 0
for i in lst:
    s += i
print(s)