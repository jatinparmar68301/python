# write a program to find out elder brother from given two brother's age.

age1=int(input("Enter age of Brother-1 : "))
age2=int(input("Enter age of Brother-2 : "))

import sys
if age1==age2:
    print("Both are same age :)")
    sys.exit()

if age1>age2:
    print("Brother-1 is Big,and the age is:",age1)
else :
    print("Brother-2 is Big,and the age is",age2)
