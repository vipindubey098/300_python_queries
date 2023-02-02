subj1 = int(input("Enter first subject marks: "))
subj2 = int(input("Enter second subject marks: "))
subj3 = int(input("Enter third subject marks: "))
subj4 = int(input("Enter fourth subject marks: "))
subj5 = int(input("Enter fifth subject marks: "))
subj6 = int(input("Enter sixth subject marks: "))

subject_total = subj1+subj2+subj3+subj4+subj5+subj6
print("Total marks of all subject is: "+str(subject_total))

total_marks_subject = 600

average_total = subject_total/total_marks_subject*100

print("Average marks of all subject is: "+str(average_total))