array = [1,2,4,5,14,53]
item = int(input("Enter element: "))
l = len(array)
ind = 0
element = 0
flg = "no"
for i in range(0,l):
    if array[i] == item:
        ind = i
        element = array[i]
        flg = "yes"

if flg == "no":
    print("Not found")
else:
    print("Element is found at: "+str(ind))