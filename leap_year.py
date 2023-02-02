# leap_year = int(input("Enter the year, you want to check: "))
# if leap_year%4 == 0:
#     print("Leap year")
# else:
#     print("Not leap year")

array = []
for i in range(5):
    array.append(int(input("Enter "+str(i+1)+" year: ")))
print(array)

for j in array:
    #print(j)
    loop_year = j
    if loop_year%4 == 0:
        print("Given "+str(loop_year)+" is leap year")
    else:
        print("Given "+str(loop_year)+" is not leap year")