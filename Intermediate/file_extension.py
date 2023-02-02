import os
file = input("Enter a file with extension: ")
file_name, file_extension = os.path.splitext(file)
print(file_name)
print(file_extension)