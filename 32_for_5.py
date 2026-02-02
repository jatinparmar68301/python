#write a program to count vowels in given string using for loop
#a e i o u 
name = input("What is your name? :")
name = name.lower() #convert and return string in lowercase
count = 0
vowels = ['a','e','i','o','u']
for letter in name: #divya
    if letter in vowels:
        count=count+1
    # print(letter,end=' ')

print(count)