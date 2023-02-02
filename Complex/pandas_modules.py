import pandas
ps = pandas.Series([1,2,3,4,5])
print(ps)
print(type(ps))
ps_list = ps.tolist()
print(ps_list)
print(type(ps_list))
print(ps_list[0:3])