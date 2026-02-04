# write a program to count words in given string 
string = "Hello Everyone MY name is Jattu Parmar. I am learning Python programming language."
words = string.split()
word_count = 0
for word in words:
    word_count = word_count + 1
print("Total number of words in the string:", word_count)
