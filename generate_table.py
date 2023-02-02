from re import I


a = int(input('Enter the number you want generate: '))

for i in range(1,11):
    b = a * i
    print(str(a)+'*'+str(i)+'='+str(b))