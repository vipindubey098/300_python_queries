# for i in range(5):
#     for j in range(i+1):
#         print("*", end="")
#     print("")
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print("")


# Invert *
height = 5
for i in range(1, height+1):
    print(height-i)
    print(i)
    print((height-i)*i)
    print(" " * (height - i)+"*"*i)