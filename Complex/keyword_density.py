para = input("Enter a para: ")
word = input("Enter a word to find density: ")
sp = 0
for i in para:
    if i == " ":
        sp += 1
total_words = sp + 1
print(total_words)
user_word = para.count(word)
print(user_word)

keyword_density = (user_word / total_words)*100
print(keyword_density)