a = set()
b = set()


for i in range(5):
    a.add(int(input("Enter a element: ")))
print(a)

for j in range(5):
    b.add(int(input("Enter b element: ")))
print(b)

#Union
u = a.union(b)
print("Union: "+str(u))

#Intersection
inter = a.intersection(b)
print("Intersection: "+str(inter))

#Difference
d = a.difference(b)
print("Difference :"+str(d))