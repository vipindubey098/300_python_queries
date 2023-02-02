import numpy
u_arr = numpy.array([3,5,6,7,8])
print(u_arr)
u_list = u_arr.tolist()
print(u_list)

add = 0
for i in u_list:
    add += i

print(add)