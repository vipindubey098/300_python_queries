input = open("input.txt","r")
output = open("output.txt","w")

for line in input:
    output.write(line)

input.close()
output.close()