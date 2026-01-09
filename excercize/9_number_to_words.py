#write a program to convert given 3 digit amount into words
# input : 175 output : one seven five 

amount= input("Enter number(3 digit :)")
amount=int(amount)

first=amount // 10 //10
print(first)

middle=amount // 10 % 10
print(middle)

last=amount % 10
print(last)

words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first]," ",words[middle]," ",words[last])
