#write a program to findout factorial of given number
#input = 5
#process = 5 x 4 x 3 x 2 x 1 
#output = 120 
number = int(input("Enter number :"))
factorial = 1 

while number>0:
    factorial = factorial * number 
    number = number - 1 #4 
print(factorial) #120