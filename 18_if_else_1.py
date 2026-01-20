'''
write a program to accept month number from user and display how many days that month has 
1    31
4    30
'''
import sys
month = int(input("Enter month (1 to 12) :"))
if month==2:
    print("this month has 28/29")
    sys.exit()
    
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("this month has 31 days")
else:
    print("this month has 30 days")
    
print('Good bye....')