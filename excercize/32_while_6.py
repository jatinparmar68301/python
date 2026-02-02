# write a program to figure out whether given number  is perfect number or not

num = int(input("Enter a number: "))

i = 1
sum = 0

while i < num:
    if num % i == 0:
        sum = sum + i
    i = i + 1

if sum == num:
    print(f"{num} is Perfect Number")
else:
    print(f"{num} is Not a Perfect Number")

 #eg of perfect number = 6 (1+2+3=6)