dict = {1:"pink",2:"grey",3:"Blue",4:"purple"}
user_key = int(input("Enter key: "))
for k in dict.keys():
    if user_key == k:
        print(str(k)+" Key is existed")
    else:
        print(str(k)+" Key isn't existed")