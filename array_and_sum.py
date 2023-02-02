array = []
for i in range(5):
    array.append(int(input("Enter "+str(i+1)+" number: ")))
print(array)

sum= 0
for j in array:
    sum += j
print(sum)