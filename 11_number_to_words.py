#write a program to convert given 2 digit amount into words
# input : 53 output five three 
#task fifty three 
amount = input("Enter number (2 digit :)") 
amount = int(amount)
last = amount % 10 #3
# print(last)
first = amount // 10 #5
# print(first)
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first]," ",words[last])