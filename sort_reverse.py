from audioop import reverse


std_marks = []
for i in range(4):
    std_marks.append(int(input("Enter student "+str(i+1)+" marks: ")))
std_marks.sort(reverse=True)
print(std_marks)
print(std_marks[2])
