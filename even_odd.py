from cmath import sqrt


num = int(input("Enter a no. :"))
if num%2 == 0:
    print("Given number i.e. "+str(num)+" is even")
else:
    print("Given number i.e. "+str(num)+" is odd")

sq = num*num
print("Square root of given no.: "+str(sq))
