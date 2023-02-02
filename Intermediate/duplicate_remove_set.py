num_set1 = set()
for i in range(5):
    item = int(input("Enter "+str(i+1)+" number set: "))
    num_set1.add(item)

print("Set 1: "+str(num_set1))

num_set2 = set()
for i in range(5):
    item = int(input("Enter "+str(i+1)+" number set: "))
    num_set2.add(item)

print("Set 1: "+str(num_set2))

print("Result: ")
rslt = num_set1.symmetric_difference(num_set2)
print(rslt)