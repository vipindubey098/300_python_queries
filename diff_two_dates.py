from datetime import datetime

date1 = input("Enter 1st date: ")
date2 = input("Enter 2nd date: ")

# date_format = "%m/%d/%Y"
date_format = "%d/%m/%Y"

d1 = datetime.strptime(date1, date_format)
d2 = datetime.strptime(date2, date_format)

diff = d2-d1

print(diff)
print(diff.days)