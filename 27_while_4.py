#write a program to print given amount into words like below
#amount = 123456
#output = one two three four five six 
amount = int(input("Enter amount : "))
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
list = [] #empty list
#get last digit of 12345

while amount>0:
    reminder = amount % 10 #5
    list.insert(0,words[reminder])
    amount = amount // 10 #1234
    reminder = amount % 10 #4

#convert list into string 
output = " ".join(list)
print(output)