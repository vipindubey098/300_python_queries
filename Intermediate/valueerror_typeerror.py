import math

name = input("Enter your name: ")
age = int(input("Enter your age: "))
nm = float(input("Enter no. of sqrt: "))

try:
    print(name+age)
except TypeError:
    print("Concetenating two different datatypes")
else:
    print("There is no error")
finally:
    print("Code is completed")


try:
    sq = math.sqrt(nm)
    print("Square root of "+str(nm)+" is "+str(sq)+"")
except ValueError:
    print("There is issue with value you are passing")