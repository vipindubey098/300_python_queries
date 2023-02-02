st = input("Enter sentence: ")
reverse_st = ""
for i in st:
    print(i)
    print(i+reverse_st)
    reverse_st = i + reverse_st
print(reverse_st)