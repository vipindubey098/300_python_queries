lst = []  #created array
for i in range(6):  #forloop, creating range of 6 length
    lst.append(int(input("Enter "+str(i+1)+" Number: "))) #appending all six data in array
 
# print(lst)

#implementing max variable as 0
# max = 0
max = 0
min = lst[0] #initializing first value of above array
#print(min)
#using array in forloop
for j in lst:
    # print(j)
    grt = j
    #print(grt)
    if grt > max:
        max = j
    if grt < min:
        min = j

print("Greater number is: "+str(max))
print("Smallest number is: "+str(min))