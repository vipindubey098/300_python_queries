import pandas as pd
lst = []
for i in range(5):
    lst.append(int(input("Enter "+str(i+1)+" no.: ")))

print(lst)
ps = pd.Series(lst)
print(ps)
new_ps = pd.Series(lst,index=['a','b','c','d','e'])
print(new_ps)