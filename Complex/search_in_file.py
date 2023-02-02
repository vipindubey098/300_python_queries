para = input("Enter a paragraph: ")
file = open("input.txt", "r+")
word = input("Enter a word: ")
lines = file.readlines()
for line in lines:
    if line.find(word) != -1:
        print("Word is existed")
    else:
        print("No word is there")
file.write(para)
file.close()