dict = {1:"pink",2:"grey",3:"purple",4:"yellow"}
#print(dict[3]) # purple
# print(dict[5]) # We will get keyerror 5

lst = ["yellow","green","blue","pink","white"]
#print(lst[3]) #pink
# print(lst[6]) #Indexerror : list out of range

# let's handle keyerror and indexerror
try:
    print(dict[6])
except KeyError:
    print("Key is not existed")

try:
    print(lst[6])
except IndexError:
    print("Index is not existed")