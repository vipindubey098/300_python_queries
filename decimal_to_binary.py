#first way
def decimaltobinary(num):
    #This function uses recursion to convert & print decimal to binary number
    if num > 1:
        decimaltobinary(num//2)
    print(num % 2, end = '')

decimal = 12
decimaltobinary(decimal)

# Second way:

def decimaltobin(value):
    if value < 0: #base case if no. is negative
        return 'not positive'
    elif value == 0: #base case if no. is zero
        return 0
    else: 
        return str(decimaltobin(value//2))+str((value%2))
print (decimaltobin(12))