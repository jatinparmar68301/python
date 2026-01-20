'''
 write a program to accept length and width of two different farm from user. and find out & display which farm is bigger 

'''

length = float(input("Enter length of farm1 :"))
width = float(input("Enter width of farm1 :"))

Total = length*width

length2 = float(input("Enter length of farm2 :"))
width2 = float(input("Enter width of farm2 :"))

Total2 = length2*width2

print(Total)
print(Total2)

if Total>Total2:
    print("Total size is",Total,"The Farm 1 is bigger ")
if Total2>Total:
    print("Total2 size is",Total2,"The Farm 2 is bigger")
if Total==Total2:
    print("Both farm is same")
print("Good By :)")