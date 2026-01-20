'''
if decision making 
         write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
        input : 15 hours 
        output  3 PM 

        input : 11 hours 
        output  11 AM 

        input : 25 hours 
        output  invalid input 
'''

hour= int(input("Enter hours(24) :"))
import sys

if hour>24:
    print("Invalid choice because not accept 24 up number !!!")
    sys.exit()
if hour<=12:
    print("time is",hour,"AM")
if hour>=12:
    print("time is",hour-12,"PM")
print("Good By :)")
